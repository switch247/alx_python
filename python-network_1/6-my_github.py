import requests
import sys

def get_user_id(username, password):
    """ read the oficial github docs to get the url"""
    # url = "https://api.github.com/users"
    url = 'https://api.github.com/user'

    # response = get(url, auth = auth.HTTPBasicAuth(username,password))
    r = requests.get(url, auth=(username, password))
    print(r.json().get('id'))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    get_user_id(username, password) 
    # url = 'https://api.github.com/user'
    # username = sys.argv[1]
    # password = sys.argv[2]
    # r = get(url, auth=auth.HTTPBasicAuth(username, password))
    # print(r.json().get('id'))

