"Keeps everyone glomped"

import requests
import json
import time
import davidsocial_login as login

session = login.session

# # INITIAL GLOMPING TO CLEAR BACKLOG

# # gets your following list
# res = requests.get(f"https://www.davidsocial.com/api/get-bootlicking?id={login.user}", cookies= session.cookies)

# # # check for errors
# res.raise_for_status()

# # load the response as a list
# following = res.json()
# # print(following)

# num = 0

# # this loop actually does all the glomping
# for i in following:
#     glomp = {
#         "message": "glompity glomp glomp",
#         "sender": login.user,
#         "receiver": i
#     }

#     res = requests.post("https://www.davidsocial.com/api/glomp", json= glomp, cookies= session.cookies)
#     num += 1
#     print(f"{num:3d}/{len(following)} initial glomp {i}")
#     # print(res)

# print("finished initial glomping\n")



# REPEATED/ADVANCED GLOMPING :)

while True:
    time.sleep(1)

    # sees if there are new notifs
    res = requests.get(f"https://www.davidsocial.com/api/check-notifications", cookies= session.cookies)
    
    if res.json()["seen"] == False:
        # tells david that notifs have been checked
        res = requests.get(f"https://www.davidsocial.com/api/seen-notifications", cookies= session.cookies)

        # gets actual contents of notifs
        res = requests.get(f"https://www.davidsocial.com/api/get-notifications-4?id={login.user}", cookies= session.cookies)

        notifs = res.json()

        unglomped = []
        for i in notifs:
            if i["type"] == "7" and i["seen"] == False:
                # add unglomped ppl to list
                unglomped.append(i["actor"])
                # mark notif as 'interacted with'
                res = requests.get(f"https://www.davidsocial.com/api/interact-with-notif?id={i['id']}", cookies= session.cookies)
        
        # print(unglomped)
        for j in unglomped:
            glomp = {
            "message": "get advanced glomped :)",
            "sender": login.user,
            "receiver": j
            }
            print(f"glomped {j} | {time.ctime()}")
            res = requests.post("https://www.davidsocial.com/api/glomp", json= glomp, cookies= session.cookies)