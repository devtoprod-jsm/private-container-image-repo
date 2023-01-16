from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return "Hello Kube!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)