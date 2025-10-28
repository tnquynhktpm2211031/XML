import requests, jsonschema

url = "http://127.0.0.1:5000/api/book"
res = requests.get(url)
data = res.json()

schema = {
    "type": "object",
    "required": ["title", "author", "price", "inStock"],
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 100},
        "author": {"type": "string"},
        "price": {"type": "number", "exclusiveMinimum": 0},
        "inStock": {"type": "boolean"},
        "categories": {"type": "array", "items": {"type": "string"}},
        "rating": {"type": "number", "minimum": 0, "maximum": 5}
    }
}

print("📘 Dữ liệu nhận được:", data)

try:
    jsonschema.validate(instance=data, schema=schema)
    print("✅ Dữ liệu hợp lệ!")
except jsonschema.ValidationError as e:
    print("❌ Dữ liệu không hợp lệ:", e.message)
