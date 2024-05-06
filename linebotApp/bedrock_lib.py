import json
import boto3
from langchain_community.chat_models import BedrockChat


def all_text_models():
    bedrock = boto3.client('bedrock', region_name='us-east-1')
    try:
        res = bedrock.list_foundation_models()['modelSummaries']
    except Exception as e:
        print(e)
        return []        
    res = filter(
        lambda x: 'TEXT' in x['inputModalities'] and 'TEXT' in x['outputModalities'], res
    )
    res = filter(
        lambda x: x['modelLifecycle']['status'] == 'ACTIVE', res
    )
    res = filter(
        lambda x: x['inferenceTypesSupported'] == ['ON_DEMAND'], res
    )
    return list(res)

def chat(content, model_id):
    llm = BedrockChat(model_id=model_id, region_name='us-east-1')
    return llm.predict(content)


if __name__ == "__main__":
    print(len(all_text_models()))
    chat("こんにちは", "amazon.titan-tg1-large")

# def call(system, user, model_id):
#     client = boto3.client('bedrock', region_name='us-east-1')
#     if "anthropic" in model_id:
#         enclosed_prompt = system + "\nHuman: " + user + "\n\nAssistant:"
#         body = {
#             "prompt": enclosed_prompt,
#             "max_tokens_to_sample": 512,
#             "temperature": 0.5,
#             "stop_sequences": ["\n\nHuman:"],
#         }
#     elif "llama" in model_id:
#         body = {
#                 "prompt": system + "\n" + user,
#                 "temperature": 0.5,
#                 "top_p": 0.9,
#                 "max_gen_len": 512,
#         }
#     elif "titan" in model_id:
#         body = {
#             "inputText": system + "\n" + user ,
#             "textGenerationConfig": {
#                 "maxTokenCount": 512,
#                 "stopSequences": ["User:"],
#                 "temperature": 0.5,
#                 "topP":0.9
#             }
#         }
#     elif "cohere" in model_id:
#         body = {
#             "prompt": system + "\n" + user ,
#             "max_tokens": 512,
#             "temperature": 0.5,
#         }       
#     else:
#         body = {
#             "prompt": system + "\n" + user ,
#             "maxTokens": 512,
#             "temperature": 0.5,
#         }
#     try:
#         response = client.invoke_model(
#             modelId=model_id,
#             body=json.dumps(body),
#             contentType="application/json",
#             accept="application/json",
#         )
#     except Exception as e:
#         print(e)
#         return f"{e}"
#     response_body = json.loads(response.get('body').read())
#     # print(response_body)
#     if response_body.get('completions'):
#         outputText = response_body.get('completions')[0].get('data')["text"]
#     elif response_body.get('generations'):
#         outputText = response_body.get('generations')[0].get('text')
#     elif response_body.get('generation'):
#         outputText = response_body.get('generation')
#     else:
#         outputText = response_body.get('results')[0].get('outputText')
#     return outputText
