from utils.http_util import HttpUtil

class MessageApi:
    """消息模块API"""
    
    @staticmethod
    def post_text(app_id, to_wxid, content, ats=""):
        """发送文本消息"""
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "content": content,
            "ats": ats
        }
        return HttpUtil.post_json("/message/postText", params)
        
    @staticmethod
    def post_file(app_id, to_wxid, file_url, file_name):
        """发送文件消息"""
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "fileUrl": file_url,
            "fileName": file_name
        }
        return HttpUtil.post_json("/message/postFile", params)
        
    @staticmethod
    def post_image(app_id, to_wxid, img_url):
        """发送图片消息"""
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "imgUrl": img_url
        }
        return HttpUtil.post_json("/message/postImage", params)
        
    @staticmethod
    def revoke_msg(app_id, to_wxid, msg_id, new_msg_id, create_time):
        """撤回消息"""
        params = {
            "appId": app_id,
            "toWxid": to_wxid,
            "msgId": msg_id,
            "newMsgId": new_msg_id,
            "createTime": create_time
        }
        return HttpUtil.post_json("/message/revokeMsg", params)
        
    @staticmethod
    def set_callback_url(app_id: str, callback_url: str) -> dict:
        """设置消息回调地址
        
        Args:
            app_id: 设备ID
            callback_url: 回调地址URL，必须以http://或https://开头
            
        Returns:
            dict: 响应结果
        """
        data = {
            "appId": app_id,
            "url": callback_url
        }
        return HttpUtil.post_json("/message/callback/set", data)
        
    @staticmethod
    def get_callback_url(app_id: str) -> dict:
        """获取当前设置的回调地址
        
        Args:
            app_id: 设备ID
            
        Returns:
            dict: 响应结果，data字段为当前的回调地址
        """
        data = {
            "appId": app_id
        }
        return HttpUtil.post_json("/message/callback/get", data) 