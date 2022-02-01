import requests

resp = requests.delete("https://reqres.in/api/users/2")
print(resp.status_code)
# print(resp.json()) #since, there is no data it will throw error.
assert resp.status_code == 204 , "User deletion failed."
