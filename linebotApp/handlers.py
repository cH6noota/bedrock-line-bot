import os

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
)
from linebot.v3.webhooks import (
    MessageEvent,
    FollowEvent,
    TextMessageContent
)
import db
from bedrock_lib import chat
from quick_reply import create_model_items, model_select


configuration = Configuration(access_token=os.getenv("ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))


@handler.add(FollowEvent)
def follow_message(event):
    if event.type == "follow":
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text='フォローありがとうございます。\nどのモデルを利用しますか？', quickReply=create_model_items())
                    ]
                )
            )

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        user_id = event.source.user_id
        text = event.message.text
        model = model_select(text)
        if model:
            db.put(user_id, model["modelId"])
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text=f'{model["modelName"]}が選択されました', quickReply=create_model_items())
                    ]
                )
            )
            return 
        user = db.get(user_id)
        if user==None:
            line_bot_api.reply_message_with_http_info(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        TextMessage(text='利用するモデルを選択してください', quickReply=create_model_items())
                    ]
                )
            )
            return
        res_text = chat(text, user["modelId"])
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=res_text, quickReply=create_model_items())]
            )
        )