import requests


SERVERLESS_ENDPOINT = "4bmg7klo3kqehruy5uddzdhuvq0rqxnd.lambda-url.us-east-1.on.aws"


def call_hello_function(data: dict):
    url = f"https://{SERVERLESS_ENDPOINT}"
    response = requests.get(url)
    return response.json()


# Example usage
data = {"name": "World"}
result = call_hello_function(data)
print(result)
