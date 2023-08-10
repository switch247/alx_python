import requests
import sys
"""
The `post_email` function sends a POST request to a specified URL with an email parameter.

:param url: The URL where the email will be posted
:param email: The email parameter is the email address that will be sent in the POST request to the
specified URL
"""

def post_email(url=sys.argv[1], email=sys.argv[2]):
    """ffhh"""
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
    __doc__="""doc for class"""
__doc__="""doc for module"""

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
