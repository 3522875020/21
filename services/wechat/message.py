from dataclasses import dataclass
from typing import Optional
from database.operations import db_manager
from services.feishu.api import feishu_api
import logging

@dataclass
class WeChatMessage:
    """微信消息"""
    msg_type: int
    content: str
    from_user: str
    to_user: str
    is_group: bool
    sender: str
    
    @classmethod
    def from_callback(cls, data: dict) -> 'WeChatMessage':
        """从回调数据创建消息对象"""
        msg_data = data.get('Data', {})
        content = msg_data.get('Content', {}).get('string', '')
        from_user = msg_data.get('FromUserName', {}).get('string', '')
        to_user = msg_data.get('ToUserName', {}).get('string', '')
        
        is_group = '@chatroom' in from_user
        sender = from_user
        
        if is_group and ':' in content:
            sender, content = content.split(':', 1)
            content = content.strip()
            
        return cls(
            msg_type=msg_data.get('MsgType'),
            content=content,
            from_user=from_user,
            to_user=to_user,
            is_group=is_group,
            sender=sender
        )
        
    def get_display_text(self) -> str:
        """获取显示文本"""
        if self.msg_type == 1:
            return self.content
        
        type_texts = {
            3: '[图片]',
            43: '[视频]',
            34: '[语音]',
            49: '[分享]',
            48: '[位置]',
            4903: '[文件]'
        }
        
        return type_texts.get(self.msg_type, f'[未知消息类型 {self.msg_type}]')

class MessageHandler:
    """消息处理器"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def handle_message(self, data: dict) -> bool:
        """处理消息"""
        try:
            message = WeChatMessage.from_callback(data)
            
            # 获取目标chat_id
            source_id = message.from_user if message.is_group else message.sender
            feishu_chat_id = db_manager.get_feishu_chat_id(source_id)
            
            if not feishu_chat_id:
                self.logger.warning(f"未找到映射关系: {source_id}")
                return False
                
            # 构造发送内容
            display_text = message.get_display_text()
            content = f"{message.sender}: {display_text}" if message.is_group else display_text
            
            # 发送到飞书
            success = feishu_api.send_message(feishu_chat_id, content)
            
            if success:
                self.logger.info(f"消息转发成功: {content}")
            else:
                self.logger.error(f"消息转发失败: {content}")
                
            return success
            
        except Exception as e:
            self.logger.error(f"处理消息失败: {str(e)}")
            return False

message_handler = MessageHandler() 