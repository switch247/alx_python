import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    body = response.text
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)

else:
    print(f"Error: {response.status_code}")
