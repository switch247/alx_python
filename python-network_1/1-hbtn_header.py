import requests
import sys

# The `get_request_id` function is defined to retrieve the value of the `X-Request-Id` header from a
# HTTP GET request to a specified URL.
def get_request_id(*argv):
    """
    The function `get_request_id` sends a GET request to a specified URL, retrieves the value of the
    'X-Request-Id' header from the response, and prints it.
    """
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
    else:
        # url = sys.argv[1]
        get_request_id(sys.argv)