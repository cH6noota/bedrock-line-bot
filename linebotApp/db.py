import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
table_name = "ParameterTable-line-bot-bedrock"
table = dynamodb.Table(table_name)

def put(user_id, model_id):
    option = {
        'Key': {'userId': user_id},
        'UpdateExpression': 'set #modelId = :model_id',
        'ExpressionAttributeNames': {
            '#modelId': 'modelId',
        },
        'ExpressionAttributeValues': {
            ':model_id': model_id
        }
    }
    table.update_item(**option)

def get(user_id):
    try:
        res = table.get_item(
            Key={
                'userId': user_id
            }
        )
        return res.get('Item')
    except:
        return None
if __name__ == "__main__":
    put("a", "cc")
    # print(get("aa"))
