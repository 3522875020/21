from flask import Flask, request, jsonify
import json
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('wechat.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

@app.route('/v2/api/callback/collect', methods=['POST'])
def wechat_callback():
    """处理微信回调消息"""
    try:
        # 获取消息内容
        data = request.get_json()
        
        # 记录消息到日志
        logging.info(f"收到新消息: {json.dumps(data, ensure_ascii=False)}")
        
        # 根据消息类型处理
        msg_type = data.get("type")
        if msg_type == 1:  # 文本消息
            handle_text_message(data)
        elif msg_type == 3:  # 图片消息
            handle_image_message(data)
        elif msg_type == 34:  # 语音消息
            handle_voice_message(data)
        elif msg_type == 43:  # 视频消息
            handle_video_message(data)
        elif msg_type == 37:  # 好友请求
            handle_friend_request(data)
        elif msg_type == 10000:  # 系统消息
            handle_system_message(data)
        else:
            logging.info(f"未处理的消息类型: {msg_type}")
            
        # 返回成功响应
        return jsonify({"ret": 200, "msg": "success"})
        
    except Exception as e:
        logging.error(f"处理消息失败: {str(e)}")
        return jsonify({"ret": 500, "msg": str(e)})

def handle_text_message(data):
    """处理文本消息"""
    try:
        from_user = data.get("fromUser")
        content = data.get("content")
        create_time = datetime.fromtimestamp(data.get("createTime", 0))
        
        logging.info(f"收到来自 {from_user} 的文本消息: {content}")
        logging.info(f"消息时间: {create_time}")
        
        # TODO: 在这里添加文本消息的处理逻辑
        # 例如:自动回复、消息转发等
        
    except Exception as e:
        logging.error(f"处理文本消息失败: {str(e)}")

def handle_image_message(data):
    """处理图片消息"""
    try:
        from_user = data.get("fromUser")
        image_url = data.get("image", {}).get("url")
        
        logging.info(f"收到来自 {from_user} 的图片消息: {image_url}")
        
        # TODO: 在这里添加图片消息的处理逻辑
        # 例如:图片保存、图片分析等
        
    except Exception as e:
        logging.error(f"处理图片消息失败: {str(e)}")

def handle_voice_message(data):
    """处理语音消息"""
    try:
        from_user = data.get("fromUser")
        voice_url = data.get("voice", {}).get("url")
        
        logging.info(f"收到来自 {from_user} 的语音消息: {voice_url}")
        
        # TODO: 在这里添加语音消息的处理逻辑
        
    except Exception as e:
        logging.error(f"处理语音消息失败: {str(e)}")

def handle_video_message(data):
    """处理视频消息"""
    try:
        from_user = data.get("fromUser")
        video_url = data.get("video", {}).get("url")
        
        logging.info(f"收到来自 {from_user} 的视频消息: {video_url}")
        
        # TODO: 在这里添加视频消息的处理逻辑
        
    except Exception as e:
        logging.error(f"处理视频消息失败: {str(e)}")

def handle_friend_request(data):
    """处理好友请求"""
    try:
        from_user = data.get("fromUser")
        content = data.get("content")
        
        logging.info(f"收到来自 {from_user} 的好友请求: {content}")
        
        # TODO: 在这里添加好友请求的处理逻辑
        # 例如:自动通过好友请求
        
    except Exception as e:
        logging.error(f"处理好友请求失败: {str(e)}")

def handle_system_message(data):
    """处理系统消息"""
    try:
        content = data.get("content")
        logging.info(f"收到系统消息: {content}")
        
        # TODO: 在这里添加系统消息的处理逻辑
        
    except Exception as e:
        logging.error(f"处理系统消息失败: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 