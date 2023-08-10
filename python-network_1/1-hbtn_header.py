import requests
import sys

try:
    response = requests.get(sys.argv[1])
    # print(response.headers)
    # print(response.text)
    request_id = response.headers.get('X-Request-Id')
    if request_id:
        # print(f"The value of X-Request-Id is: {request_id}")
        print(request_id)
    else:
        print("X-Request-Id header not found in the response.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

__doc__="""doc for module"""
