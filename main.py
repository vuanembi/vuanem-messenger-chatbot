from flask import Flask

from messenger.controller import messenger_controller

app = Flask(__name__)

app.register_blueprint(messenger_controller, url_prefix="/messenger")


@app.route("/", methods=["GET", "POST"])
def receive_message():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
