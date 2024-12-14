import sqlite3
import logging
from database.operations import db_manager
from services.feishu.api import feishu_api

class MappingManager:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def add_mapping(self, source_id: str, name: str, type: str = 'group'):
        """添加新的映射关系"""
        try:
            # 连接数据库
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            
            # 检查是否已存在
            cursor.execute(
                "SELECT target_id FROM chat_mappings WHERE source_id = ?", 
                (source_id,)
            )
            result = cursor.fetchone()
            
            if result:
                self.logger.info(f"映射已存在: {source_id} -> {result[0]}")
                return result[0]
            
            # 创建飞书群组
            chat_id = self._create_feishu_chat(name)
            if not chat_id:
                return None
            
            # 添加映射
            cursor.execute("""
                INSERT INTO chat_mappings (source_id, target_id, name, type)
                VALUES (?, ?, ?, ?)
            """, (source_id, chat_id, name, type))
            
            conn.commit()
            self.logger.info(f"添加新映射: {source_id} -> {chat_id}")
            return chat_id
            
        except Exception as e:
            self.logger.error(f"添加映射失败: {str(e)}")
            return None
        finally:
            conn.close()
    
    def _create_feishu_chat(self, name: str) -> str:
        """创建飞书群组"""
        try:
            url = "https://open.feishu.cn/open-apis/im/v1/chats"
            
            data = {
                "name": name,
                "description": f"微信群 {name} 的消息同步",
                "chat_mode": "group",
                "chat_type": "private"
            }
            
            response = requests.post(
                url,
                headers=feishu_api._get_headers(),
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                if result.get('code') == 0:
                    return result['data']['chat_id']
                    
            self.logger.error(f"创建飞书群组失败: {response.text}")
            return None
            
        except Exception as e:
            self.logger.error(f"创建飞书群组异常: {str(e)}")
            return None

mapping_manager = MappingManager() 