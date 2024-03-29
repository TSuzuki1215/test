import os

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('yomhFOrz8noQkz3IvixK7h5iZFh4WmWrxULizVZawEFg/svL8UomirZtPIHxLhKeuhOLSEetj6LybUTRn9uERyPwPiBd5axkb7v3/iZ2ccCjXSKCuYqVhRZgT8o5H+xC2Peg5c3Rr1t9QxN+wfU/MQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3151776a13d758b378dbdd845c8d5a44')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    app.run()

#test1
