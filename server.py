from flask import Flask, request, jsonify
import json
import logging
from datetime import datetime
from collections import deque
from farpush.feishu_api import feishu_api
from farpush.User_push import get_chat_id_by_nickname
from farpush.groups_push import get_chat_id_by_chatroomname

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

# 使用双端队列存储最近10条消息的MsgId
message_cache = deque(maxlen=10)

@app.route('/v2/api/callback/collect', methods=['POST'])
def collect_callback():
    try:
        # 获取POST请求中的数据
        data = request.get_json()
        
        # 将数据转换为格式化的JSON字符串
        formatted_data = json.dumps(data, indent=2, ensure_ascii=False)
        
        # 记录时间戳
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 输出到终端和日志
        print(f"\n[{timestamp}] 收到新消息:")
        print(formatted_data)
        logging.info(f"收到新消息: {formatted_data}")

        # 解析消息内容
        msg_data = data.get('Data', {})
        msg_type = msg_data.get('MsgType')
        content = msg_data.get('Content', {}).get('string', '')
        from_user = msg_data.get('FromUserName', {}).get('string', '')
        to_user = msg_data.get('ToUserName', {}).get('string', '')

        # 判断是否为群消息
        is_chatroom = '@chatroom' in from_user
        
        # 如果是群消息，解析发送者昵称和内容
        if is_chatroom and ':' in content:
            sender_wxid, text = content.split(':', 1)
            text = text.strip()
        else:
            sender_wxid = from_user
            text = content

        # 根据消息类型设置显示文本
        if msg_type == 1:  # 文本消息
            display_text = text
        elif msg_type == 3:  # 图片
            display_text = '[图片]'
        elif msg_type == 43:  # 视频
            display_text = '[视频]'
        elif msg_type == 34:  # 语音
            display_text = '[语音]'
        elif msg_type == 49:  # 分享
            display_text = '[分享]'
        elif msg_type == 48:  # 位置
            display_text = '[位置]'
        elif msg_type == 4903:  # 文件
            display_text = '[文件]'
        else:
            display_text = f'[未知消息类型 {msg_type}]'

        # 转发消息到飞书
        if is_chatroom:
            # 群消息
            feishu_chat_id = get_chat_id_by_chatroomname(from_user)
            if feishu_chat_id:
                formatted_message = f"{sender_wxid}: {display_text}"
                logging.info(f"尝试转发群消息到飞书: {formatted_message}")
                if feishu_api.send_text(feishu_chat_id, formatted_message):
                    logging.info(f"群消息转发成功: {formatted_message}")
                else:
                    logging.error(f"群消息转发失败: {formatted_message}")
            else:
                logging.error(f"未找到群聊 {from_user} 对应的飞书chat_id")
        else:
            # 私聊消息
            feishu_chat_id = get_chat_id_by_nickname(sender_wxid)
            if feishu_chat_id:
                logging.info(f"尝试转发私聊消息到飞书 from {sender_wxid}: {display_text}")
                if feishu_api.send_text(feishu_chat_id, display_text):
                    logging.info(f"私聊消息转发成功 from {sender_wxid}: {display_text}")
                else:
                    logging.error(f"私聊消息转发失败 from {sender_wxid}: {display_text}")
            else:
                logging.warning(f"未找到用户 {sender_wxid} 对应的飞书chat_id")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error(f"处理消息失败: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 