from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/smsResponse")
def hanlde_response():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=int("80"),debug=True)