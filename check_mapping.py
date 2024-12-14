import sqlite3
import logging

def check_database_mapping():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 检查群聊映射
        cursor.execute("SELECT * FROM chatroom_groups")
        chatrooms = cursor.fetchall()
        print("\n群聊映射:")
        for room in chatrooms:
            print(f"ChatRoomName: {room[1]}, chat_id: {room[2]}")
            
        # 检查用户映射
        cursor.execute("SELECT * FROM user_groups")
        users = cursor.fetchall()
        print("\n用户映射:")
        for user in users:
            print(f"NickName: {user[1]}, chat_id: {user[2]}")
            
    except Exception as e:
        print(f"检查数据库失败: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    check_database_mapping() 