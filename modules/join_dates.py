"Prints a list of all users, sorted by the date they joined"

import requests
import json
import time
import davidsocial_login as login

session = login.session


ls = requests.get("https://www.davidsocial.com/api/get-user-list", cookies= session.cookies)

ls = ls.json()


ls = sorted(ls, key= lambda i :i["joinDate"])

print

for i in ls:
    print(f"{i["name"]:30} | {i["joinDate"]}")