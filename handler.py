import json


def hello(event, _context):
    name = event.get("name", "you")
    body_str = event.get("body")
    body = json.loads(body_str)
    print(body)

    name = body.get("name", "you")

    data = {
        "message": f"Hello, {name}!"}

    return {"statusCode": 200, "body": json.dumps(data)}
