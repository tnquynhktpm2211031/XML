from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Xin chào từ Flask trên mọi địa chỉ IP!"

# --- API cho bài 9.1 ---
@app.route('/api/book', methods=['GET'])
def get_book():
    book = {
        "title": "Học Python cơ bản",
        "author": "Nguyễn Minh",
        "price": 120000,
        "inStock": True,
        "categories": ["Lập trình", "Python", "Cơ bản"],
        "rating": 4.5
    }
    return jsonify(book)

# --- API cho bài 9.2 ---
@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    users = {
        "minh123": {
            "username": "minh123",
            "password": "Abc@1234",
            "emails": ["minh123@example.com", "backup@gmail.com"],
            "age": 16,
            "address": {"city": "Cần Thơ", "street": "45 Nguyễn Trãi"},
            "hobbies": ["đọc sách", "chơi game"],
            "isVerified": False
        },
        "lan456": {
            "username": "lan456",
            "password": "Xyz@5678",
            "emails": ["lan456@example.com"],
            "age": 18,
            "address": {"city": "Hà Nội"},
            "hobbies": ["vẽ", "nghe nhạc"]
        }
    }
    return jsonify(users.get(username, {"error": "User not found"}))

# --- API phép trừ ---
@app.route('/api/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "a và b phải là số"}), 400
    return jsonify({"result": a - b})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
