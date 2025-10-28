import requests, jsonschema

url = "http://127.0.0.1:5000/api/user/minh123"
res = requests.get(url)
data = res.json()

schema = {
    "type": "object",
    "required": ["username", "password", "emails", "age", "address"],
    "properties": {
        "username": {"type": "string", "pattern": "^[a-zA-Z0-9]+$"},
        "password": {"type": "string", "minLength": 8},
        "emails": {"type": "array", "items": {"type": "string", "format": "email"}},
        "age": {"type": "integer", "minimum": 13, "maximum": 100},
        "address": {"type": "object", "required": ["city"]}
    }
}

print("👤 Dữ liệu nhận được:", data)

try:
    jsonschema.validate(instance=data, schema=schema)
    print("✅ Dữ liệu hợp lệ!")
except jsonschema.ValidationError as e:
    print("❌ Dữ liệu không hợp lệ:", e.message)
