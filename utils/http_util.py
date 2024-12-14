import requests
import json

class HttpUtil:
    # 直接配置
    BASE_URL = "http://39.107.192.142:2531/v2/api"  # 替换为实际服务器地址
    DEBUG = True  # 是否打印调试信息
    _token = None  # 私有类变量存储token
    
    @classmethod
    def set_token(cls, token):
        """设置token"""
        cls._token = token
        
    @classmethod
    def get_token(cls):
        """获取token"""
        return cls._token
    
    @classmethod
    def post_json(cls, route, params):
        """发送POST请求
        
        Args:
            route: API路由
            params: 请求参数字典
            
        Returns:
            响应JSON对象
        """
        headers = {
            "Content-Type": "application/json"
        }
        if cls._token:
            headers["X-GEWE-TOKEN"] = cls._token
            
        try:
            if not cls.BASE_URL:
                raise Exception("BASE_URL未配置")
                
            url = cls.BASE_URL + route
            resp = requests.post(url, 
                               json=params,
                               headers=headers,
                               timeout=30)  # 添加超时设置
            
            resp_json = resp.json()
            
            # 仅在debug模式下打印详细信息
            if cls.DEBUG:
                print(json.dumps(resp_json, indent=2))
            
            if resp_json["ret"] == 200:
                return resp_json
            else:
                raise Exception(f"API错误: {resp.text}")
                
        except requests.exceptions.Timeout:
            print(f"请求超时: {url}")
            raise
        except requests.exceptions.RequestException as e:
            print(f"请求异常: {url}")
            print(f"异常信息: {str(e)}")
            raise
        except Exception as e:
            print(f"其他错误: {url}")
            print(f"错误信息: {str(e)}")
            raise