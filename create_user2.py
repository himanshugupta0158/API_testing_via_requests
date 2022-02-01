import requests
import json

# reading data.json file data
user_data = open("data.json" , "r").read()

# passing data to url to create new user.
resp = requests.post("https://reqres.in/api/users" , data=json.loads(user_data))
print(resp)
print(resp.json())
assert resp.json()['job'] == 'Python Dev'
print(resp.headers.get("Content-Type"))






