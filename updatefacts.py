import requests
import davidsocial_login as login
import json

session = login.session

"""
ALLOWS YOU TO UPDATE THE FACTS SECTION WITH CUSTOM TEXT
"""

prompts = {
	"Prompt": "Answer",
	"Prompt": "Answer",
	"Prompt": "Answer",
	"Prompt": "Answer",
	"Prompt": "Answer",
	"Prompt": "Answer",
	"Prompt": "Answer",
}
facts = {"facts": json.dumps(prompts)}



res = requests.post("https://www.davidsocial.com/api/update-facts", json=facts, cookies=session.cookies)
print(res)
