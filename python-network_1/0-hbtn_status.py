import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code == 200:
    body = response.text
    lines = body.split("\n")
    for line in lines:
        print(f"\t- {line}")
else:
    print(f"Error: {response.status_code}")
