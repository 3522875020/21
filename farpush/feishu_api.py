import requests
import json
import logging
import os
from dotenv import load_dotenv
from token_manager import token_manager
from typing import Optional

# 加载.env文件
load_dotenv()

class FeishuAPI:
    """飞书API封装类"""
    
    BASE_URL = "https://open.feishu.cn/open-apis"
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app_id = os.getenv('FEISHU_APP_ID')
        self.app_secret = os.getenv('FEISHU_APP_SECRET')
        
        if not self.app_id or not self.app_secret:
            raise ValueError("请在.env文件中设置 FEISHU_APP_ID 和 FEISHU_APP_SECRET")
            
        # 设置token manager的配置
        token_manager.set_config(self.app_id, self.app_secret)
    
    def _get_headers(self) -> dict:
        """获取请求头"""
        token = token_manager.get_token()
        if not token:
            raise Exception("无法获取有效的飞书Token")
        
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json; charset=utf-8"
        }
    
    def send_message(self, chat_id: str, content: str, msg_type: str = "text") -> bool:
        """
        发送消息到飞书
        
        Args:
            chat_id: 会话ID
            content: 消息内容
            msg_type: 消息类型，默认为text
            
        Returns:
            bool: 发送是否成功
        """
        try:
            url = f"{self.BASE_URL}/im/v1/messages"
            params = {"receive_id_type": "chat_id"}
            
            # 根据消息类型格式化content
            if msg_type == "text":
                content = json.dumps({"text": content})
            
            data = {
                "receive_id": chat_id,
                "msg_type": msg_type,
                "content": content
            }
            
            self.logger.debug(f"发送消息到飞书: {json.dumps(data, ensure_ascii=False)}")
            
            response = requests.post(
                url, 
                params=params,
                headers=self._get_headers(),
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0:
                    self.logger.info("消息发送成功")
                    return True
                else:
                    self.logger.error(f"发送消息失败: {result.get('msg')}")
            else:
                self.logger.error(f"HTTP请求失败: {response.status_code} {response.text}")
            
            return False
            
        except Exception as e:
            self.logger.error(f"发送消息异常: {str(e)}")
            return False
    
    def send_text(self, chat_id: str, text: str) -> bool:
        """发送文本消息"""
        return self.send_message(chat_id, text, "text")
    
    def send_image(self, chat_id: str, image_key: str) -> bool:
        """发送图片消息"""
        content = json.dumps({"image_key": image_key})
        return self.send_message(chat_id, content, "image")
    
    def send_file(self, chat_id: str, file_key: str) -> bool:
        """发送文件消息"""
        content = json.dumps({"file_key": file_key})
        return self.send_message(chat_id, content, "file")

# 创建全局实例
feishu_api = FeishuAPI() 