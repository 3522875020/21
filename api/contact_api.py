from utils.http_util import HttpUtil

class ContactApi:
    """联系人模块API"""
    
    @staticmethod
    def fetch_contacts_list(app_id):
        """获取通讯录列表"""
        params = {
            "appId": app_id
        }
        return HttpUtil.post_json("/contacts/fetchContactsList", params)
        
    @staticmethod
    def get_brief_info(app_id, wxids):
        """获取联系人简要信息"""
        params = {
            "appId": app_id,
            "wxids": wxids
        }
        return HttpUtil.post_json("/contacts/getBriefInfo", params)
        
    @staticmethod
    def get_detail_info(app_id, wxids):
        """获取联系人详细信息"""
        params = {
            "appId": app_id,
            "wxids": wxids
        }
        return HttpUtil.post_json("/contacts/getDetailInfo", params)
        
    @staticmethod
    def search(app_id, contacts_info):
        """搜索联系人"""
        params = {
            "appId": app_id,
            "contactsInfo": contacts_info
        }
        return HttpUtil.post_json("/contacts/search", params) 