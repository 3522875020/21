import requests
import json
import time
import logging
from typing import Optional

class TokenManager:
    def __init__(self):
        self.app_id = None
        self.app_secret = None
        self._token = None
        self._token_expires = 0
        self.logger = logging.getLogger(__name__)
    
    def set_config(self, app_id: str, app_secret: str):
        """设置飞书应用配置"""
        self.app_id = app_id
        self.app_secret = app_secret
    
    def get_token(self) -> Optional[str]:
        """获取访问令牌，如果过期则自动刷新"""
        if not self.app_id or not self.app_secret:
            self.logger.error("未设置 APP_ID 或 APP_SECRET")
            return None
            
        now = time.time()
        if self._token and now < self._token_expires - 60:  # 提前60秒刷新
            return self._token
            
        try:
            url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
            data = {
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }
            
            response = requests.post(url, json=data)
            if response.status_code == 200:
                result = response.json()
                if result.get("code") == 0:
                    self._token = result.get("tenant_access_token")
                    self._token_expires = now + result.get("expire", 7200)
                    return self._token
                else:
                    self.logger.error(f"获取Token失败: {result.get('msg')}")
            else:
                self.logger.error(f"HTTP请求失败: {response.status_code}")
                
        except Exception as e:
            self.logger.error(f"获取Token异常: {str(e)}")
            
        return None

token_manager = TokenManager() 