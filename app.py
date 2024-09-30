from flask import Flask, request

from 根据域名获取cname或者A记录解析 import get_record

app = Flask(__name__)


@app.route('/getRecord', methods=['GET', 'POST'])
def getRecord():
    domain = request.args.get('domain')
    type = request.args.get('type', default='CNAME')
    record = get_record(domain, type)
    return record


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)
