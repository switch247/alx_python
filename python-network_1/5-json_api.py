import sys
import requests
def search_user(letter):
    """ test"""
    url = f"http://0.0.0.0:5000/search_user"
    params = {"q": letter}
    try:
        response =  requests.post(url, data=params)
        data = response.json()
        # print(data)
        # print(response.params)
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
        # else:
            # print("Not a valid JSON")
    except Exception as e:
        print("Not a valid JSON")
        # print ("failed to connect")

    

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    # print(letter)
    search_user(letter)
