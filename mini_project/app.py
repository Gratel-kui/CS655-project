from flask import Flask
from flask import request
from flask_cors import *  # 注意这一行-01

import Service

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['POST', 'GET'])
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    f = request.files.get('file')
    print("upload request")

    path = './images/files/1.png'
    f.save(path)

    caption = Service.imageToText(path)
    # caption = "this"

    return caption


@app.route('/getfiles', methods=['GET'])
def get_files():
    f = open()


if __name__ == '__main__':
    app.run(host="10.10.1.2", port=8080)


