from api.group_api import GroupApi
from api.message_api import MessageApi
import os
import json
import logging

class WeChatInfoManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.app_id = os.getenv('DEVICE_ID')
        
    def get_groups_info(self):
        """获取所有群聊信息"""
        try:
            response = GroupApi.get_groups_list(self.app_id)
            if response and response.get('code') == 0:
                groups = response.get('data', {}).get('groups', [])
                return [{
                    'source_id': group.get('groupId'),
                    'name': group.get('nickName', '未命名群聊'),
                    'type': 'group'
                } for group in groups]
            else:
                self.logger.error(f"获取群聊列表失败: {response}")
                return []
        except Exception as e:
            self.logger.error(f"获取群聊信息异常: {str(e)}")
            return []
            
    def get_contacts_info(self):
        """获取所有联系人信息"""
        try:
            response = MessageApi.get_contacts_list(self.app_id)
            if response and response.get('code') == 0:
                contacts = response.get('data', {}).get('contacts', [])
                return [{
                    'source_id': contact.get('wxid'),
                    'name': contact.get('nickName', '未知用户'),
                    'type': 'user'
                } for contact in contacts]
            else:
                self.logger.error(f"获取联系人列表失败: {response}")
                return []
        except Exception as e:
            self.logger.error(f"获取联系人信息异常: {str(e)}")
            return []
            
    def update_mappings(self):
        """更新映射关系"""
        mappings = []
        
        # 获取群聊信息
        groups = self.get_groups_info()
        if groups:
            mappings.extend(groups)
            self.logger.info(f"获取到 {len(groups)} 个群聊信息")
            
        # 获取联系人信息
        contacts = self.get_contacts_info()
        if contacts:
            mappings.extend(contacts)
            self.logger.info(f"获取到 {len(contacts)} 个联系人信息")
            
        # 保存到配置文件
        if mappings:
            config_path = 'config/mappings.py'
            with open(config_path, 'w', encoding='utf-8') as f:
                f.write('DEFAULT_MAPPINGS = ')
                f.write(json.dumps(mappings, ensure_ascii=False, indent=4))
                f.write('\n')
            self.logger.info(f"更新了 {len(mappings)} 个映射关系")
        
        return mappings

wechat_info = WeChatInfoManager() 