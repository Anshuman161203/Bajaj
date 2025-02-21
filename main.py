from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get("data", [])
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
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
        return jsonify({"is_success": False, "message": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
