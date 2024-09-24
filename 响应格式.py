from flask import Flask, make_response, json, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/index')
def index():
    data = {'name': '张三'}
    # response = make_response(json.dumps(data, ensure_ascii=False))
    # response.mimetype = 'application/json;charset=utf-8'
    # return response
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
