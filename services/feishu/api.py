import requests
import json
import logging
from typing import Optional
from config.settings import FEISHU_APP_ID, FEISHU_APP_SECRET
from .token import token_manager

class FeishuAPI:
    """飞书API封装"""
    
    BASE_URL = "https://open.feishu.cn/open-apis"
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
        if not FEISHU_APP_ID or not FEISHU_APP_SECRET:
            raise ValueError("请在.env文件中设置 FEISHU_APP_ID 和 FEISHU_APP_SECRET")
            
        token_manager.set_config(FEISHU_APP_ID, FEISHU_APP_SECRET)
    
    def send_message(self, chat_id: str, content: str, msg_type: str = "text") -> bool:
        """发送消息到飞书"""
        try:
            url = f"{self.BASE_URL}/im/v1/messages"
            
            headers = {
                "Authorization": f"Bearer {token_manager.get_token()}",
                "Content-Type": "application/json; charset=utf-8"
            }
            
            data = {
                "receive_id": chat_id,
                "msg_type": msg_type,
                "content": json.dumps({"text": content}) if msg_type == "text" else content
            }
            
            response = requests.post(
                url, 
                params={"receive_id_type": "chat_id"},
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                success = result.get('code') == 0
                if not success:
                    self.logger.error(f"发送消息失败: {result.get('msg')}")
                return success
                
            self.logger.error(f"HTTP请求失败: {response.status_code} {response.text}")
            return False
            
        except Exception as e:
            self.logger.error(f"发送消息异常: {str(e)}")
            return False

feishu_api = FeishuAPI() 