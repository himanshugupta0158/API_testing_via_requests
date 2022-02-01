import requests

# Basic Authentication

# succesful
resp = requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('admin','admin'))
print(resp.status_code)

# unsuccessful
resp2 = requests.get(
    "https://the-internet.herokuapp.com/basic_auth", auth=('abcd', 'abcd'))
print(resp2.status_code)
