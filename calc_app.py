from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route("/calculator", methods=["POST"])
def calculator():
    """
    This function will take a payload in below format and beahve like a calculator to give the answer
    {
        "num1": NUMBER,
        "num2": NUMBER,
        "operator": "OPERATOR" - this can be add, sub, mul, div
    }
    """
    # Storing the payload in data
    data = request.get_json()

    try:
        if data is None:
            return jsonify({"error": "No JSON data provided"}), 400
        # Getting both the numbers from payload
        num1 = data.get("num1")
        num2 = data.get("num2")
        
        
        if num1 is None or num2 is None:
            return jsonify({"error": "Both num1 and num2 are required"}), 400
        
        operator = data.get("operator")
        # Getting the operator from payload
        if operator is None:
            return jsonify({"error": "Operator is required"}), 400
        
        # Logic to filter the operator
        if operator == "add":
            result = num1 + num2
        elif operator == "sub":
            result = num1 - num2
        elif operator == "mul":
            result = num1 * num2
        elif operator == "div":
            result = num1 / num2
        else:
            return jsonify({"error": "Invalid operator"}), 400
        

        return jsonify({"Answer": result})
    
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Main function
if __name__ == '__main__':
    app.run(debug=True)  # Important for development!