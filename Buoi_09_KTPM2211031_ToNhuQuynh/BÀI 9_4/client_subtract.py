import requests

url = "http://127.0.0.1:5000/api/subtract"
payload = {"a": 10, "b": 3}
res = requests.post(url, json=payload)

print("🧮 Kết quả:", res.json())
import requests

url = "http://127.0.0.1:5000/api/subtract"
payload = {"a": 10, "b": 3}
res = requests.post(url, json=payload)

print("🧮 Kết quả:", res.json())
