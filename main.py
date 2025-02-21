from flask import Flask, request, jsonify
from flask_cors import CORS  # Allow cross-origin requests

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        if not request.json or "data" not in request.json:
            return jsonify({"is_success": False, "message": "Invalid request, 'data' key missing"}), 400
        
        data = request.json["data"]

        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "'data' should be a list"}), 400

        numbers = [item for item in data if isinstance(item, str) and item.isdigit()]
        alphabets = [item for item in data if isinstance(item, str) and item.isalpha()]
        highest_alphabet = max(alphabets, key=str.upper) if alphabets else ""

        response = {
            "is_success": True,
            "user_id": "anshuman_roshan_1607",  
            "email": "22bcs14129@cuchd.in",
            "roll_number": "22BCS14129",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
