from flask import Flask
app = Flask(__name__)

from twilio.twiml.messaging_response import MessagingResponse

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/smsResponse", methods=['GET', 'POST'])
def handle_response():
	resp = MessagingResponse()
	resp.message("Hello Jon Carmack")
	return str(resp)

if __name__ == "__main__":
    app.run(debug=True)