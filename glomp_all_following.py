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


# this loop actually does all the glomping
for i in following:
    glomp = {
        "message": "You have been glomped using DS Tools",
        "sender": login.user,
        "receiver": i
    }

    res = requests.post("https://www.davidsocial.com/api/glomp", json= glomp, cookies= session.cookies)
    # print(res)

print("finished glomping")
