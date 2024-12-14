from dataclasses import dataclass

@dataclass
class ChatMapping:
    """聊天映射关系"""
    id: int
    source_id: str    # 微信ID
    target_id: str    # 飞书chat_id
    name: str         # 名称
    type: str         # 类型：user/group
    avatar: str       # 头像 