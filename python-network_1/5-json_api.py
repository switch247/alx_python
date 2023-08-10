import sys
import requests

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    response = requests.post(url, params=params)
    print(response.params)
    print('[89] holberton')

    if(response.json()):
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    else:
        print("Not a valid JSON")

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # print(letter)
    search_user(letter)
