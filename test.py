import requests

s = requests.Session()
s.trust_env = True

r = s.get("https://fota-server-v1-0.onrender.com")

print(r.status_code)