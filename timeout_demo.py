import requests 

r = requests.get("https://httpbin.org/delay/3" , timeout=5)
print(r.status_code)

r2 = requests.get("https://httpbin.org/delay/5" , timeout=3)
print(r2.status_code)



