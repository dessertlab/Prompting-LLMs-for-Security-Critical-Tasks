from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    user_agent = request.headers.get('User-Agent')
    return f"<html><body><h1>Your User-Agent is: {user_agent}</h1></body></html>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
