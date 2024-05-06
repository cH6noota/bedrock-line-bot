import json, os
import logging

from linebot.v3.exceptions import (
    InvalidSignatureError
)
import handlers

logger = logging.getLogger()

def lambda_handler(event, context):
    print(event["headers"])
    signature = event["headers"].get('X-Line-Signature')
    if signature==None:
        signature = event["headers"].get('x-line-signature')
    # get request body as text
    body = event["body"]
    print("Request body: " + body)
    try:
        handlers.handler.handle(body, signature)
    except InvalidSignatureError:
        logger.info("Invalid signature. Please check your channel access token/channel secret.")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "ok",
        }),
    }
