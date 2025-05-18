import requests

try:
    import logins
    login_info = True
except:
    login_info = False

"""
THIS FILE IS ONLY USED TO LOGIN AND CREATE THE RIGHT COOKIE
"""

# checks to see if server is online
res = requests.get('https://www.davidsocial.com/api/ping')
# print(res.status_code)

if res.status_code != 200:
    print("init ping went wrong")
    quit()
else:
    print("init ping good")


"""
if you don't want to manually login every time, make a file called 'logins.py' in this folder
with the variables 'user' and 'password' set to your login info (as strings btw).
this will automatically log you in every time
"""
# login
if login_info:
    user = logins.user
    password = logins.password
else:
    user = input("username: ")
    password = input("password: ")

login_credentials = {"username": user, "password": password}

session = requests.post('https://www.davidsocial.com/api/login', json=login_credentials)

if session.status_code != 200:
    print("login didnt work")
else:
    print("logged in")



