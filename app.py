from flask import Flask, jsonify
import json
from asyncio import run
from message_bus import MessageBus  # assuming azure_code.py contains the MessageBus class

app = Flask(__name__)


@app.route('/', methods=['GET'])
def root():
    message_bus = MessageBus()
    message_body = json.dumps({"json": "object"})  # JSON object you'd like to send
    run(message_bus.send(message=message_body, correlation_id="1234"))
    return jsonify({"message": "Hello, Azure!"})


if __name__ == "__main__":
    app.run(debug=True)
