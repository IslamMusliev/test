from flask import Flask, request
import os
import uuid

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    return request.host

@app.route('/author', methods=['GET'])
def get_author():
    return os.getenv('AUTHOR')

@app.route('/id', methods=['GET'])
def get_id():
    return os.getenv('UUID', str(uuid.uuid4()))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
