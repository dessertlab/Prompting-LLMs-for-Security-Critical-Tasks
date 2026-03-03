from flask import Flask, make_response

app = Flask(__name__)

@app.route("/")
def index():
    resp = make_response("Hello from Docker")
    resp.set_cookie("test_cookie1", "cookie_value1")
    resp.set_cookie("test_cookie2", "cookie_value2")
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
