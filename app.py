from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'User')
    age = request.args.get('age', 'unknown')
    return f"Hello {name}, you are {age} years old."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
