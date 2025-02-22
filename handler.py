import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def hola_mundo(event, context):
    body = {
        "message": "Hola Mundo!",
        "input": event,
    }
    
    response = {"statusCode": 200, "body": json.dumps(body)}
    
    return response