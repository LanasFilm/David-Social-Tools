"Glomps everyone in the user's following list"

import requests
import json
import davidsocial_login as login

session = login.session

# gets your following list
res = requests.get(f"https://www.davidsocial.com/api/get-bootlicking?id={login.user}", cookies= session.cookies)

# check for errors
res.raise_for_status()

# load the response as a list
following = res.json()
# print(following)

num = 0

# this loop actually does all the glomping
for i in following:
    glomp = {
        "message": "",
        "sender": login.user,
        "receiver": i
    }

    res = requests.post("https://www.davidsocial.com/api/glomp", json= glomp, cookies= session.cookies)
    num += 1
    print(f"{num:3d}/{len(following)} glomped {i}")
    # print(res)

print("finished glomping")
