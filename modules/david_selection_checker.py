"Checks a user's posts history, and returns posts which have been marked by David Intelligence"
"Recycled and slightly modified code from search_user.py"

import requests
import json
import time
import davidsocial_login as login

session = login.session

user = input("Enter user: ")

# gets all of selected user's posts
res = requests.get(f"https://www.davidsocial.com/api/user-posts?username={user}", cookies= session.cookies)
ls = res.json()

# checks if user exists
if not ls:
    print("User doesn't exist, or hasn't made any posts yet")
    time.sleep(2)
    quit()



# finds if post has been selected
matching_posts = []
for i in range(len(ls)):
    post = ls[i]
    # print(post)

    if post["david_selection"]:
        matching_posts.append(i)


# puts post in chronological order
matching_posts.reverse()
    

# print out of found posts
if matching_posts:
    print("\nDAVID SELECTED POSTS: \n")
    for i in matching_posts:
        print(ls[i]["content"])

        if ls[i]["attached_image"]:
            print("***THERE IS AN ATTACHED IMAGE***")

        print(f"https://www.davidsocial.com/~/thread/{ls[i]["id"]}")
        print("-"*100)
else:
    print("\nNO DAVID SELECTED POSTS FOUND \n")