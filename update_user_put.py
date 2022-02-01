import requests
import json

""" 
PUT : 
put focus on whole updation of data if limit is not applied or given.
if data exist -> then data will be updated.
if data does not exist -> then new data wil be created using 
data for updation.
{
    "name": "Mukesh",
    "job": "Python Dev",
    "Address": "Chennai"
}

PATCH : 
In patch - specifically only the properties that you want to update.
if data not exist -> then it will not update it.
in patch , we can update data partially.

{
    "name": "Jake"
}
"""

payload = {
    "name": "morpheus",
    "job": "zion resident"
}
payload1 = {
    "name" : "APIGuy"
}

resp = requests.put("https://reqres.in/api/users/2" , data=payload)
resp1 = requests.patch("https://reqres.in/api/users/2" , data=payload1)
print(resp)
print(resp.json())
print(resp.json()['job'])
assert resp.json()['job']=="zion resident"

print(resp1)
print(resp1.json())
print(resp1.json()['name'])
assert resp1.json()['name']=="APIGuy"





