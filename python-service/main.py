from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet(name):
    return jsonify(message="Hello, World! " + name)

@app.route('/hello', methods=['POST'])
def hello(name):
    user = {
        "username": name,
        "email": "john@example.com",
        "roles": ["admin", "user"],
        "isActive": True
    }
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True, port=8080)