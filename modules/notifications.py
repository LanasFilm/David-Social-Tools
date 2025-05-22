"System to detect notifications; not completed right now"

import requests
import json
import time # for testing purposes

import davidsocial_login as login

session = login.session



old_check = requests.post("https://www.davidsocial.com/api/my-notifications", cookies=session.cookies)
old_check = json.loads(old_check.content) # converts it to python string




def new_notifs() -> list:
    new_notifs = []
    global old_check

    new_check = requests.post("https://www.davidsocial.com/api/my-notifications", cookies=session.cookies)
    new_check = json.loads(new_check.content) # converts to python string
    try:
        if new_check != old_check:
            print("new notifications")
            for i in new_check:
                if not i in old_check:
                    new_notifs.append(i)
                else:
                    break

        old_check = new_check

        return new_notifs
    except:
        print("something went wrong??")
        return []


"""
CURRENTLY UNFINISHED, BUT THE "news" VARIABLE BELOW GIVES YOU NEW NOTIFICATIONS
YOU CAN JUST USE THIS FILE, AND PLUG IN THE OUTPUT OF NEWS TO WHATEVER YOU LIKE
WILL TRY TO MAKE THIS DO SOMETHING LATER
"""

while True:
    news = new_notifs()
    print(news)
    time.sleep(5)