from flask import Flask, request, jsonify
import json
import logging
from config.settings import LOG_FORMAT, LOG_FILE
from services.wechat.message import message_handler

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

@app.route('/v2/api/callback/collect', methods=['POST'])
def collect_callback():
    try:
        data = request.get_json()
        
        # 记录原始消息
        logging.info(f"收到新消息: {json.dumps(data, indent=2, ensure_ascii=False)}")
        
        # 处理消息
        success = message_handler.handle_message(data)
        
        return jsonify({
            "status": "success" if success else "failed"
        }), 200
        
    except Exception as e:
        logging.error(f"处理消息失败: {str(e)}")
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 