from api.login_api import LoginApi
import time
import base64
import qrcode
import json
import os
from PIL import Image
import io
from dotenv import load_dotenv
from api.message_api import MessageApi
from utils.http_util import HttpUtil
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

def save_env_vars(device_id=None, wxid=None, token=None):
    """保存环境变量到.env文件
    
    Args:
        device_id: 设备ID
        wxid: 微信ID
        token: 接口token
    """
    # 读取现有的.env内容
    env_content = {}
    if os.path.exists('.env'):
        load_dotenv()
        for key in os.environ:
            env_content[key] = os.environ[key]
    
    # 更新需要保存的变量
    if device_id:
        env_content['DEVICE_ID'] = device_id
    if wxid:
        env_content['WXID'] = wxid
    if token:
        env_content['TOKEN'] = token
    
    # 写入.env文件
    with open('.env', 'w', encoding='utf-8') as f:
        for key, value in env_content.items():
            f.write(f'{key}={value}\n')
    
    print(f"环境变量已保存到.env")

def load_env_vars():
    """加载环境变量
    
    Returns:
        dict: 包含device_id、wxid和token的字典
    """
    load_dotenv()
    return {
        'device_id': os.getenv('DEVICE_ID'),
        'wxid': os.getenv('WXID'),
        'token': os.getenv('TOKEN')
    }

def save_qr_image(base64_str, file_path):
    """保存二维码图片
    
    Args:
        base64_str: base64编码的图片数据
        file_path: 保存路径
    """
    # 移除base64编码头部
    if "base64," in base64_str:
        base64_str = base64_str.split("base64,")[1]
    
    # 解码并保存图片
    img_data = base64.b64decode(base64_str)
    with open(file_path, "wb") as f:
        f.write(img_data)

def display_qr_in_terminal(qr_data):
    # 创建QR码对象
    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.make()
    
    # 获取QR码的模块矩阵
    matrix = qr.get_matrix()
    
    # 在终端打印QR码
    for row in matrix:
        line = ''
        for cell in row:
            if cell:
                line += '██'  # 黑色块使用两个全角方块
            else:
                line += '  '  # 白色块使用两个空格
        print(line)

def save_login_info(app_id, login_info):
    """保存登录信息到文件
    
    Args:
        app_id: 应用ID
        login_info: 登录信息字典
    """
    data = {
        'app_id': app_id,
        'wxid': login_info['wxid'],
        'nickname': login_info['nickName'],
        'mobile': login_info['mobile'],
        'login_time': time.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # 确保目录存在
    if not os.path.exists('data'):
        os.makedirs('data')
        
    # 保存到JSON文件
    file_path = 'data/login_info.json'
    try:
        if os.path.exists(file_path):
            # 如果文件存在，读取现有数据
            with open(file_path, 'r', encoding='utf-8') as f:
                saved_data = json.load(f)
        else:
            saved_data = []
            
        # 检查是否已存在相同的wxid
        exists = False
        for item in saved_data:
            if item['wxid'] == data['wxid']:
                item.update(data)  # 更新现有数据
                exists = True
                break
                
        if not exists:
            saved_data.append(data)  # 添加新数据
            
        # 保存更新后的数据
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(saved_data, f, ensure_ascii=False, indent=2)
            
        print(f"\n登录信息已保存到 {file_path}")
        
    except Exception as e:
        print(f"保存登录信息失败: {str(e)}")

def login_test():
    """登录测试流程"""
    try:
        # 1. 获取已保存的设备ID
        env_vars = load_env_vars()
        device_id = env_vars['device_id']
        
        if not device_id:
            print("请先登录获取设备ID")
            return
        
        # 2. 获取token
        print("获取token...")
        resp = LoginApi.get_token()
        token = resp["data"]
        print(f"获取token成功: {token}")
        
        # 设置获取到的token
        HttpUtil.set_token(token)
        
        # 3. 检查在线状态
        print("\n检查在线状态...")
        resp = LoginApi.check_online(device_id)
        is_online = resp["data"]
        if not is_online:
            print("设备离线，无法登录!")
            return
        
        # 4. 获取登录二维码
        print("\n获取登录二维码...")
        resp = LoginApi.get_qr(device_id)  # 使用保存的设备ID
        qr_data = resp["data"]
        app_id = qr_data["appId"]
        
        uuid = qr_data["uuid"]
        qr_img_base64 = qr_data["qrImgBase64"]
        
        # 保存二维码图片
        save_qr_image(qr_img_base64, "login_qr.jpg")
        print(f"二维码已保存到login_qr.jpg")
        print(f"appId: {app_id}")
        print(f"uuid: {uuid}")
        
        # 在获取二维码数据后调用
        qr_url = resp['data']['qrData']  # 获取二维码URL
        display_qr_in_terminal(qr_url)
        
        # 5. 循环检查登录状态
        print("\n请使用手机微信扫描二维码登录...")
        max_retry = 30  # 最大重试次数
        retry_count = 0
        
        while retry_count < max_retry:
            try:
                resp = LoginApi.check_qr(app_id, uuid, "")
                login_status = resp["data"]["status"]
                
                if login_status == 2:  # 登录成功
                    login_info = resp["data"]["loginInfo"]
                    print("\n登录成功!")
                    print(f"微信号: {login_info['wxid']}")
                    print(f"昵称: {login_info['nickName']}")
                    print(f"手机号: {login_info['mobile']}")
                    
                    # 保存wxid
                    save_env_vars(wxid=login_info['wxid'])
                    
                    # 保存登录信息到JSON
                    save_login_info(app_id, login_info)
                    break
                    
                elif login_status == 1:  # 已扫码
                    print("已扫码,等待确认...")
                    
                else:  # 等待扫码
                    print("等待扫码...")
                    
            except Exception as e:
                print(f"检查登录状态出错: {str(e)}")
                
            retry_count += 1
            time.sleep(2)  # 每2秒检查一次
            
        if retry_count >= max_retry:
            print("\n登录超时!")
            return
            
    except Exception as e:
        print(f"登录测试出错: {str(e)}")

class MessageHandler(BaseHTTPRequestHandler):
    """消息处理器"""
    
    def do_POST(self):
        """处理POST请求"""
        try:
            # 获取消息内容
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            message = json.loads(post_data.decode('utf-8'))
            
            # 处理消息
            self.handle_message(message)
            
            # 返回成功响应
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"ret": 200, "msg": "success"}).encode())
            
        except Exception as e:
            print(f"处理消息失败: {str(e)}")
            self.send_response(500)
            self.end_headers()
    
    def handle_message(self, message):
        """处理接收到的消息
        
        Args:
            message: 消息字典
        """
        try:
            print("\n收到新消息:")
            print(json.dumps(message, ensure_ascii=False, indent=2))
            
            # 这里可以根据消息类型进行不同的处理
            msg_type = message.get("type")
            if msg_type == 1:  # 文本消息
                self.handle_text_message(message)
            elif msg_type == 3:  # 图片消息
                self.handle_image_message(message)
            # 可以添加更多消息类型的处理...
            
        except Exception as e:
            print(f"处理消息详情失败: {str(e)}")
    
    def handle_text_message(self, message):
        """处理文本消息"""
        try:
            content = message.get("content")
            from_user = message.get("fromUser")
            print(f"收到来自 {from_user} 的文本消息: {content}")
            
            # 这里可以添加自动回复等功能
            
        except Exception as e:
            print(f"处理文本消息失败: {str(e)}")
    
    def handle_image_message(self, message):
        """处理图片消息"""
        try:
            from_user = message.get("fromUser")
            image_url = message.get("image", {}).get("url")
            print(f"收到来自 {from_user} 的图片消息: {image_url}")
            
        except Exception as e:
            print(f"处理图片消息失败: {str(e)}")

def start_message_server(port=2531):
    """启动消息服务器
    
    Args:
        port: 服务器端口号
    """
    try:
        server = HTTPServer(('', port), MessageHandler)
        print(f"\n消息服务器已启动，监听端口: {port}")
        server.serve_forever()
        
    except Exception as e:
        print(f"启动消息服务器失败: {str(e)}")

def test_callback():
    """测试设置回调地址"""
    try:
        # 从.env加载环境变量
        env_vars = load_env_vars()
        device_id = env_vars['device_id']
        token = env_vars['token']
        
        if not device_id:
            print("请先登录获取设备ID")
            return
            
        if not token:
            print("未获取到token，请先登录")
            return
            
        # 设置回调地址
        callback_url = "http://39.107.192.142:8080/v2/api/callback/collect"
        print(f"\n设置回调地址: {callback_url}")
        resp = LoginApi.set_callback(token, callback_url)
        print(f"设置结果: {resp}")
        
        # 启动消息监听服务器
        message_thread = threading.Thread(target=start_message_server)
        message_thread.daemon = True  # 设置为守护线程
        message_thread.start()
        
        # 保持主线程运行
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n程序已停止")
        
    except Exception as e:
        print(f"设置回调地址失败: {str(e)}")

if __name__ == "__main__":
    # 1. 先检查在线状态
    env_vars = load_env_vars()
    device_id = env_vars['device_id']
    
    if device_id:
        print("设备ID已存在，检查在线状态...")
        # 确保token已设置
        token = env_vars['token']
        if not token:
            print("未获取到token，请先登录")
        else:
            HttpUtil.set_token(token)  # 设置token
            resp = LoginApi.check_online(device_id)
            is_online = resp["data"]
            if is_online:
                print("设备在线，直接设置回调地址...")
                test_callback()
            else:
                print("设备离线，无法设置回调地址。")
    else:
        # 2. 如果没有设备ID，则进行登录
        login_test()