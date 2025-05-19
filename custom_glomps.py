import requests
import json
import time
import davidsocial_login as login

session = login.session


while True:
    target = input("Target of glomp: ")

    # checks if target exists
    res = requests.get(f"https://www.davidsocial.com/api/profile?username={target}", cookies= session.cookies)
    # print(res.json())
    if not res.json():
        print("User does not exist, try again")
        continue


    # checks to see if you're able to glomp this person
    check_glomp = {
        "sender": login.user, 
        "receiver": target, 
        "message":""}

    res = requests.post("https://www.davidsocial.com/api/already-glomped", json= check_glomp, cookies= session.cookies)
    if res.json() == True:
        print("\nYou cannot currently glomp this person\nPlease wait for them to glomp you back")
        time.sleep(2)
        quit()
    elif res.json() == False:
        print("You can glomp this person")
        break


# takes your message and sends it
message = input("Message: ")

glomp = {
    "message": message,
    "sender": login.user,
    "receiver": target
}

res = requests.post("https://www.davidsocial.com/api/glomp", json= glomp, cookies= session.cookies)