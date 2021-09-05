
from flask import Flask, jsonify, request

app = Flask(__name__)



@app.route('/api/captcha/postimage', methods=['POST')
def get_incomes():
    content = request.get_json()
    base64 = content['base64']
    captcha = content['captcha']
    return jsonify(incomes)


@app.route('/api/captcha/decode', methods=['POST'])
def add_income():
    content = request.get_json()
    base64 = content['base64']
    return '', 204
