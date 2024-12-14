from utils.http_util import HttpUtil

class GroupApi:
    """群聊模块API"""
    
    @staticmethod
    def create_chatroom(app_id, wxids):
        """创建群聊"""
        params = {
            "appId": app_id,
            "wxids": wxids
        }
        return HttpUtil.post_json("/group/createChatroom", params)
        
    @staticmethod
    def modify_chatroom_name(app_id, chatroom_name, chatroom_id):
        """修改群名称"""
        params = {
            "appId": app_id,
            "chatroomName": chatroom_name,
            "chatroomId": chatroom_id
        }
        return HttpUtil.post_json("/group/modifyChatroomName", params)
        
    @staticmethod
    def get_chatroom_info(app_id, chatroom_id):
        """获取群信息"""
        params = {
            "appId": app_id,
            "chatroomId": chatroom_id
        }
        return HttpUtil.post_json("/group/getChatroomInfo", params) 