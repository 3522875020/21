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
        
        # 获取消息ID
        msg_id = data.get('msgId')
        
        # 检查消息是否已经处理过
        if msg_id in message_cache:
            logging.info(f"消息 {msg_id} 已经处理过，忽略")
            return jsonify({"status": "success", "message": "duplicate message"}), 200
            
        # 将新消息ID添加到缓存
        message_cache.append(msg_id)
        
        # 将数据转换为格式化的JSON字符串
        formatted_data = json.dumps(data, indent=2, ensure_ascii=False)
        
        # 记录时间戳
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # 输出到终端和日志
        print(f"\n[{timestamp}] 收到新消息:")
        print(formatted_data)
        logging.info(f"收到新消息: {formatted_data}")

        # 解析消息内容
        msg_type = data.get('type')
        content = data.get('content', '')
        from_user = data.get('fromUser', '')
        from_nickname = data.get('fromNickName', '')
        chatroom_id = data.get('chatroomId')

        # 根据消息类型设置显示文本
        text = content
        if msg_type in [3, 47]:  # 图片或表情
            text = '[图片]'
        elif msg_type == 43:  # 视频
            text = '[视频]'
        elif msg_type == 34:  # 语音
            text = '[语音]'
        elif msg_type == 49:  # 分享
            text = '[分享]'
        elif msg_type == 48:  # 位置
            text = '[位置]'
        elif msg_type == 4903:  # 文件
            text = '[文件]'
        elif msg_type == 4922:  # 红包
            text = '[红包]'
        elif msg_type == 4923:  # 转账
            text = f'[转账] {content}'

        # 转发消息到飞书
        if msg_type == 1:  # 文本消息
            if chatroom_id:
                # 群消息
                feishu_chat_id = get_chat_id_by_chatroomname(chatroom_id)
                if feishu_chat_id:
                    formatted_message = f"{from_nickname}: {text}"
                    if feishu_api.send_text(feishu_chat_id, formatted_message):
                        logging.info(f"群消息转发成功: {formatted_message}")
                    else:
                        logging.error(f"群消息转发失败: {formatted_message}")
            else:
                # 私聊消息
                feishu_chat_id = get_chat_id_by_nickname(from_nickname)
                if feishu_chat_id:
                    if feishu_api.send_text(feishu_chat_id, text):
                        logging.info(f"私聊消息转发成功 from {from_nickname}: {text}")
                    else:
                        logging.error(f"私聊消息转发失败 from {from_nickname}: {text}")
                else:
                    logging.warning(f"未找到用户 {from_nickname} 对应的飞书chat_id")

        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error(f"处理消息失败: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 