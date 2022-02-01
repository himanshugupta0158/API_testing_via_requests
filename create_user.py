import requests

# payload or Json data

payload = {
    "name": "morpheus",
    "job": "Automation"
}

# print(type(payload))
resp = requests.post("https://reqres.in/api/users" , data=payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'Automation'

# This is creating/register new user

data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
resp2 = requests.post("https://reqres.in/api/register" , data=data)
print(resp2)
print(resp2.json()['token'])

