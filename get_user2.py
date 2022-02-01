import requests

# Validating Data

p = {"page" : 2}

resp = requests.get("https://reqres.in/api/users?" , params=p)
print(resp.url)
json_response = resp.json()

print(json_response['total'])
assert json_response['total'] == 12

print(json_response['total_pages'])
assert json_response['total_pages'] == 2 , "total pages count is not matching"

print(json_response["data"][0]["email"])
assert (json_response["data"][0]["email"]).endswith("reqres.in") , "email format is not matching."

print(json_response["data"][2]["first_name"])
print(json_response["data"][2]["last_name"])

assert json_response["data"][2]["last_name"] != None

print(json_response["support "]["url"])
