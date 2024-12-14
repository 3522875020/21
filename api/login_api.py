from utils.http_util import HttpUtil

class LoginApi:
    """登录模块API"""
    
    @staticmethod
    def get_token():
        """获取token"""
        return HttpUtil.post_json("/tools/getTokenId", {})
        
    @staticmethod
    def set_callback(token, callback_url):
        """设置回调地址"""
        params = {
            "token": token,
            "callbackUrl": callback_url
        }
        return HttpUtil.post_json("/tools/setCallback", params)
        
    @staticmethod
    def get_qr(app_id):
        """获取登录二维码"""
        params = {
            "appId": app_id
        }
        return HttpUtil.post_json("/login/getLoginQrCode", params)
        
    @staticmethod 
    def check_qr(app_id, uuid, captch_code):
        """确认登录"""
        params = {
            "appId": app_id,
            "uuid": uuid,
            "captchCode": captch_code
        }
        return HttpUtil.post_json("/login/checkLogin", params)
        
    @staticmethod
    def check_online(app_id):
        """检查是否在线"""
        params = {
            "appId": app_id
        }
        return HttpUtil.post_json("/login/checkOnline", params)
        
    @staticmethod
    def logout(app_id):
        """退出登录"""
        params = {
            "appId": app_id
        }
        return HttpUtil.post_json("/login/logout", params) 