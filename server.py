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

# 在文件开头添加消息类型常量
class MessageType:
    Unknown = 0
    Text = 1
    Image = 3
    Voice = 34
    Video = 43
    Contact = 42
    Emoji = 47
    Location = 48
    Link = 49
    File = 4903
    MiniApp = 4925
    Transfer = 4923
    RedPacket = 4922
    RoomInvitation = 4921
    AppMsg = 4920
    VideoAccount = 4919
    Revoke = 4918
    Pat = 4917

@app.route('/v2/api/callback/collect', methods=['POST'])
def wechat_callback():
    """处理微信回调消息"""
    try:
        data = request.get_json()
        logging.info(f"收到新消息: {json.dumps(data, ensure_ascii=False)}")
        
        # 根据消息类型处理
        msg_type = data.get("Data", {}).get("MsgType")
        
        handlers = {
            MessageType.Text: handle_text_message,
            MessageType.Image: handle_image_message, 
            MessageType.Voice: handle_voice_message,
            MessageType.Video: handle_video_message,
            MessageType.Contact: handle_contact_message,
            MessageType.Emoji: handle_emoji_message,
            MessageType.Location: handle_location_message,
            MessageType.Link: handle_link_message,
            MessageType.File: handle_file_message,
            MessageType.MiniApp: handle_miniapp_message,
            MessageType.Transfer: handle_transfer_message,
            MessageType.RedPacket: handle_redpacket_message,
            MessageType.RoomInvitation: handle_room_invitation_message,
            MessageType.AppMsg: handle_app_message,
            MessageType.VideoAccount: handle_video_account_message,
            MessageType.Revoke: handle_revoke_message,
            MessageType.Pat: handle_pat_message,
            37: handle_friend_request,
            10000: handle_system_message
        }
        
        handler = handlers.get(msg_type)
        if handler:
            handler(data.get("Data", {}))
        else:
            logging.info(f"未处理的消息类型: {msg_type}")
            
        return jsonify({"ret": 200, "msg": "success"})
        
    except Exception as e:
        logging.error(f"处��消息失败: {str(e)}")
        return jsonify({"ret": 500, "msg": str(e)})

def handle_text_message(data):
    """处理文本消息"""
    try:
        from_user = data.get("FromUserName", {}).get("string")
        content = data.get("Content", {}).get("string")
        create_time = datetime.fromtimestamp(data.get("CreateTime", 0))
        
        logging.info(f"收到来自 {from_user} 的文本消息: {content}")
        logging.info(f"消息时间: {create_time}")
        
        # 自动回复示例
        if content == "ding":
            # TODO: 调用发送消息API
            pass
            
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

def handle_link_message(data):
    """处理链接消息"""
    try:
        from_user = data.get("fromUser") 
        title = data.get("title")
        description = data.get("description")
        url = data.get("url")
        
        logging.info(f"收到来自 {from_user} 的链接消息:")
        logging.info(f"标题: {title}")
        logging.info(f"描述: {description}")
        logging.info(f"链接: {url}")
        
    except Exception as e:
        logging.error(f"处理链接消息失败: {str(e)}")

def handle_miniapp_message(data):
    """处理小程序消息"""
    try:
        from_user = data.get("fromUser")
        title = data.get("title")
        app_id = data.get("appId")
        
        logging.info(f"收到来自 {from_user} 的小程序消息:")
        logging.info(f"标题: {title}")
        logging.info(f"小程序ID: {app_id}")
        
    except Exception as e:
        logging.error(f"处理小程序消息失败: {str(e)}")

def handle_contact_message(data):
    """处理名片消息"""
    try:
        from_user = data.get("fromUser")
        contact_name = data.get("contact", {}).get("nickName")
        contact_wxid = data.get("contact", {}).get("wxid")
        
        logging.info(f"收到来自 {from_user} 的名片消息:")
        logging.info(f"名片昵称: {contact_name}")
        logging.info(f"名片wxid: {contact_wxid}")
        
    except Exception as e:
        logging.error(f"处理名片消息失败: {str(e)}")

def handle_emoji_message(data):
    """处理表情消息"""
    try:
        from_user = data.get("fromUser")
        emoji_url = data.get("emoji", {}).get("url")
        emoji_md5 = data.get("emoji", {}).get("md5")
        
        logging.info(f"收到来自 {from_user} 的表情消息:")
        logging.info(f"表情URL: {emoji_url}")
        logging.info(f"表情MD5: {emoji_md5}")
        
    except Exception as e:
        logging.error(f"处理表情消息失败: {str(e)}")

def handle_location_message(data):
    """处理位置消息"""
    try:
        from_user = data.get("fromUser")
        location = data.get("location", {})
        title = location.get("title")
        address = location.get("address") 
        latitude = location.get("latitude")
        longitude = location.get("longitude")
        
        logging.info(f"收到来自 {from_user} 的位置消息:")
        logging.info(f"位置名称: {title}")
        logging.info(f"详细地址: {address}")
        logging.info(f"经纬度: {latitude},{longitude}")
        
    except Exception as e:
        logging.error(f"处理位置消息失败: {str(e)}")

def handle_file_message(data):
    """处理文件消息"""
    try:
        from_user = data.get("fromUser")
        file_info = data.get("file", {})
        file_name = file_info.get("name")
        file_url = file_info.get("url")
        file_size = file_info.get("size")
        
        logging.info(f"收到来自 {from_user} 的文件消息:")
        logging.info(f"文件名: {file_name}")
        logging.info(f"文件URL: {file_url}")
        logging.info(f"文件大小: {file_size}")
        
    except Exception as e:
        logging.error(f"处理文件消息失败: {str(e)}")

def handle_transfer_message(data):
    """处理转账消息"""
    try:
        from_user = data.get("fromUser")
        transfer = data.get("transfer", {})
        amount = transfer.get("amount")
        status = transfer.get("status")
        
        logging.info(f"收到来自 {from_user} 的转账消息:")
        logging.info(f"金额: {amount}")
        logging.info(f"状态: {status}")
        
    except Exception as e:
        logging.error(f"处理转账消息失败: {str(e)}")

def handle_redpacket_message(data):
    """处理红包消息"""
    try:
        from_user = data.get("fromUser")
        redpacket = data.get("redPacket", {})
        type = redpacket.get("type")
        wish = redpacket.get("wish")
        
        logging.info(f"收到来自 {from_user} 的红包消息:")
        logging.info(f"红包类型: {type}")
        logging.info(f"祝福语: {wish}")
        
    except Exception as e:
        logging.error(f"处理红包消息失败: {str(e)}")

def handle_room_invitation_message(data):
    """处理群邀请消息"""
    try:
        from_user = data.get("fromUser")
        room_name = data.get("roomName")
        inviter = data.get("inviter")
        
        logging.info(f"收到来自 {from_user} 的群邀请消息:")
        logging.info(f"群名: {room_name}")
        logging.info(f"邀请人: {inviter}")
        
    except Exception as e:
        logging.error(f"处理群邀请消息失败: {str(e)}")

def handle_app_message(data):
    """处理应用消息"""
    try:
        from_user = data.get("fromUser")
        app_info = data.get("app", {})
        title = app_info.get("title")
        desc = app_info.get("desc")
        
        logging.info(f"收到来自 {from_user} 的应用消息:")
        logging.info(f"标题: {title}")
        logging.info(f"描述: {desc}")
        
    except Exception as e:
        logging.error(f"处理应用消息失败: {str(e)}")

def handle_video_account_message(data):
    """处理视频号消息"""
    try:
        from_user = data.get("fromUser")
        video = data.get("videoAccount", {})
        title = video.get("title")
        desc = video.get("desc")
        
        logging.info(f"收到来自 {from_user} 的视频号消息:")
        logging.info(f"标题: {title}")
        logging.info(f"描述: {desc}")
        
    except Exception as e:
        logging.error(f"处理视频号消息失败: {str(e)}")

def handle_revoke_message(data):
    """处理撤回消息"""
    try:
        from_user = data.get("fromUser")
        msg_id = data.get("msgId")
        
        logging.info(f"收到来自 {from_user} 的消息撤回:")
        logging.info(f"撤回消息ID: {msg_id}")
        
    except Exception as e:
        logging.error(f"处理撤回消息失败: {str(e)}")

def handle_pat_message(data):
    """处理拍一拍消息"""
    try:
        from_user = data.get("fromUser")
        to_user = data.get("toUser")
        
        logging.info(f"{from_user} 拍了拍 {to_user}")
        
    except Exception as e:
        logging.error(f"处理拍一拍消息失败: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 