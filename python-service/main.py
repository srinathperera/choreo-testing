from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    return jsonify(message="Hello, World! " + name)

@app.route('/hello', methods=['POST'])
def hello():
    name = request.args.get('name', 'World')  # Default to 'World' if no name is provided
    user = {
        "username": name,
        "email": "john@example.com",
        "roles": ["admin", "user"],
        "isActive": True
    }
    return jsonify(user)


if __name__ == '__main__':
    app.run(debug=True, port=8080)