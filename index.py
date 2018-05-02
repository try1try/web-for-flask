# coding:utf-8
# 引入app配置
import os
from flask import jsonify  # JSON
from flask import render_template #读取页面
from flask import Flask
import json
app = Flask(__name__)
#首页
@app.route('/')
def zwyx_dd_view():
    return render_template('index.html')
@app.route('/first')
def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
    data = json.load(open(json_url))
    print data
    return jsonify(data)
@app.route('/third')
def thirdjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
    data = json.load(open(json_url))
    print data
    return jsonify(data)
@app.route('/second')
def secondjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "as.json")
    data = json.load(open(json_url))
    print data['data']
    return jsonify(data['data'])
# 入口
if __name__ == '__main__':
    # 调试模式
    app.debug = True
    # 外部可访问的服务器
    app.run(host='127.0.0.1')
