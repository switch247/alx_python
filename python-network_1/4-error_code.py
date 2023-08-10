import requests
import sys

# The `get_request_id` function is defined to retrieve the value of the `X-Request-Id` header from a
# HTTP GET request to a specified URL.
def get_request_id(*argv):
    """
    The function `get_request_id` sends a GET request to a specified URL, retrieves the value of the
    'X-Request-Id' header from the response, and prints it.
    """

    response = requests.get(sys.argv[1])

    print( f"Error code: {response.status_code}")



        

    __doc__="""doc for class"""
__doc__="""doc for module"""
        

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
    else:
        # url = sys.argv[1]
        # print(sys.argvd)
        get_request_id(sys.argv)
