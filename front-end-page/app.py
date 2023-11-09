from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 为所有路由启用CORS

@app.route('/extract-words', methods=['POST', 'OPTIONS'])
def extract_words():
    if request.method == 'OPTIONS':
        # 对于OPTIONS请求，直接返回响应，Flask-CORS会处理头部
        return jsonify({}), 200

    # POST请求处理
    # 检查请求中是否有JSON数据
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()

    # 检查'sentence'键是否在JSON数据中
    if 'sentence' not in data:
        return jsonify({"error": "No sentence key found in JSON data"}), 400

    sentence = data['sentence']

    # 检查是否是字符串类型
    if not isinstance(sentence, str) or not sentence:
        return jsonify({"error": "Invalid input string"}), 400

    # 提取前三个字符，如果字符串长度小于3，将返回整个字符串
    extracted = sentence[:3]

    # 返回提取的结果
    return jsonify({'extracted_words': extracted})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
