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
def collect_callback():
    # 获取POST请求中的数据
    data = request.get_json()
    
    # 将数据转换为格式化的JSON字符串
    formatted_data = json.dumps(data, indent=2, ensure_ascii=False)
    
    # 记录时间戳
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # 输出到终端
    print(f"\n[{timestamp}] 收到新消息:")
    print(formatted_data)
    
    # 同时记录到日志文件
    logging.info(f"收到新消息: {formatted_data}")
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 