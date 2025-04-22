# encoding: utf-8
import uuid
import time
import requests
from flask import Flask, request, jsonify
from auth_util import gen_sign_headers
from flask_cors import CORS

APP_ID = '2025802261'
APP_KEY = 'MtJDOAqjvfQiwmFW'
URI = '/vivogpt/completions'
DOMAIN = 'api-ai.vivo.com.cn'
METHOD = 'POST'

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    json_data = request.get_json()
    user_input = json_data.get('message', '')

    if not user_input:
        return jsonify({'error': 'message is required'}), 400

    # 构造请求参数
    params = {
        'requestId': str(uuid.uuid4())
    }
    data = {
        'prompt': user_input,
        'model': 'vivo-BlueLM-TB-Pro',
        'sessionId': str(uuid.uuid4()),
        'extra': {
            'temperature': 0.9
        }
    }

    headers = gen_sign_headers(APP_ID, APP_KEY, METHOD, URI, params)
    headers['Content-Type'] = 'application/json'

    url = f'https://{DOMAIN}{URI}'

    try:
        start_time = time.time()
        response = requests.post(url, json=data, headers=headers, params=params)
        response.raise_for_status()
        res_obj = response.json()

        if res_obj['code'] == 0 and res_obj.get('data'):
            content = res_obj['data']['content']
            return jsonify({
                'response': content,
                'timecost': round(time.time() - start_time, 2)
            })
        else:
            return jsonify({'error': res_obj.get('msg', 'Unknown error')}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
