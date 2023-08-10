"""
asfasdfadadfdafgs
"""
import requests

url = "https://alu-intranet.hbtn.io/status"
response = requests.get(url)

if response.status_code <= 400:
    body = response.text
    print(response.text)

else:
    print(f"Error code: {response.status_code}")
