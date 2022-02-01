import requests

resp = requests.get("https://reqres.in/api/users?page=2")
# print(resp)
# print(type(resp))
# print(dir(resp))

code = resp.status_code
assert code == 200 , "Code doesn't match"
# print(resp.text) #return data in string format
# print(resp.content) #return data in bytes format
print(resp.json()) #return data in serialized json format
print(type(resp.headers))
print("Headers : ",resp.headers)
print("Cookies : ",resp.cookies)
print("Encoding : ",resp.encoding)
print("URLs : ",resp.url)
