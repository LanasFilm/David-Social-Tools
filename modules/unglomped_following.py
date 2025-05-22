"Gives a list of unglomped accounts that user is following"

import requests
import json
import davidsocial_login as login

session = login.session

# gets your following list
res = requests.get(f"https://www.davidsocial.com/api/get-bootlicking?id={login.user}", cookies= session.cookies)

# check for errors
res.raise_for_status()

# load the response as a list
following = res.content
# print(following)

ls = []

for i in following:

    # checks to see if you're able to glomp this person
    check_glomp = {
        "sender": login.user, 
        "receiver": i, 
        "message":""}

    res = requests.post("https://www.davidsocial.com/api/already-glomped", json= check_glomp, cookies= session.cookies)
    # adds to list if unglomped
    if res.json() == False:
        ls.append(i)

print(ls)
