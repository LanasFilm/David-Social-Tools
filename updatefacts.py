import requests
import davidsocial_login as login

session = login.session

"""
ALLOWS YOU TO UPDATE THE FACTS SECTION WITH CUSTOM TEXT
"""

# look up how python strings work if you are getting errors or want to understand this
# the actual "facts" section/content is just a giant string of text with special syntax, even though it looks like a dictionary
# i think commas tell the website when to create a new line
# colons tell it when to stop the bold text
# backslash in front of the quotation marks is just how you tell python you want the character, but don't want to start/end a string 
facts = {"facts":
            """{\"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            \"Prompt\":\"Answer\",
            """}



res = requests.post("https://www.davidsocial.com/api/update-facts", json=facts, cookies=session.cookies)
print(res)