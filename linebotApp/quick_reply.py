
from bedrock_lib import all_text_models
from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage,
    QuickReply,
    QuickReplyItem,
    MessageAction
)
import boto3 ,random

models = []

def create_model_items():
    global models
    items = []
    if len(models)==0:
        models =all_text_models() 
    for item in models:
        items.append(
            QuickReplyItem(
                action=MessageAction(
                    label=item['modelName'][-20:],
                    text=item['modelId']
                )
            )
        )

    items = random.sample(items, 13)
    quick_reply = QuickReply(items=items)
    return quick_reply


def model_select(model_id):
    global models
    if len(models)==0:
        models =all_text_models() 
    for model in models:
        if model_id == model["modelId"]:
            return model
    return None
if __name__ =="__main__":
    print(create_model_items())