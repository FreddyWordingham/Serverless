import json


def hello(event, _context):
    print()
    print(event)
    print()

    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
