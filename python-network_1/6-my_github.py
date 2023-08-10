import requests
import sys

def get_user_id(username, password):
    """ read the oficial github docs to get the url"""
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url, auth= (username,password))

    if response.status_code == 200:
        user_data = response.json()
        return user_data['id']
    else:
        # print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    user_id = get_user_id(username, password)
    print(f"{user_id}")
