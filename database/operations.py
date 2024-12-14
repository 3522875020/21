import sqlite3
from typing import Optional
from .models import ChatMapping
from config.settings import DATABASE_PATH

class DatabaseManager:
    def __init__(self):
        self.db_path = DATABASE_PATH
        self._init_database()

    def _init_database(self):
        """初始化数据库"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS chat_mappings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_id TEXT NOT NULL,
                    target_id TEXT NOT NULL,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    avatar TEXT
                )
            ''')
            conn.commit()

    def get_feishu_chat_id(self, source_id: str) -> Optional[str]:
        """获取飞书chat_id"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT target_id FROM chat_mappings WHERE source_id = ?", 
                (source_id,)
            )
            result = cursor.fetchone()
            return result[0] if result else None

db_manager = DatabaseManager() 