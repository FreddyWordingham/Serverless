import requests


SERVERLESS_ENDPOINT = "http://localhost:3000"


def call_hello_function(data: dict):
    url = f"http://localhost:3000/dev/hello"
    response = requests.post(url, json=data)
    return response.json()


# Example usage
data = {"name": "World"}
result = call_hello_function(data)
print(result)
