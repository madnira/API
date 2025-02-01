from flask import Flask , request , jsonify
import logging
app = Flask(__name__)

# Configure the logging
logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@app.route("/calculator2", methods=["POST"])
def calculator():
    """
    This function will take a payload in below format and beahve like a calculator to give the answer
    {
        "num1": NUMBER,
        "num2": NUMBER,
        "operator": "OPERATOR" - this can be add, sub, mul, div
    }

    This will also has the logger function
    """
    # Storing the payload in data
    data = request.get_json()
    logging.info(f"Received data: {data}")

    try:
        if data is None:
            logging.error("No JSON data provided")
            return jsonify({"error": "No JSON data provided"}), 400
        # Getting both the numbers from payload
        num1 = data.get("num1")
        num2 = data.get("num2")
        
        
        if num1 is None or num2 is None:
            logging.error("Both num1 and num2 are required")
            return jsonify({"error": "Both num1 and num2 are required"}), 400
        
        operator = data.get("operator")
        # Getting the operator from payload
        if operator is None:
            logging.error("Operator is required")
            return jsonify({"error": "Operator is required"}), 400
        
        # Logic to filter the operator
        if operator == "add":
            result = num1 + num2
            logging.info(f"Addition done")
        elif operator == "sub":
            result = num1 - num2
            logging.info(f"Subtraction done")
        elif operator == "mul":
            result = num1 * num2
            logging.info(f"Multiplication done")
        elif operator == "div":
            result = num1 / num2
            logging.info(f"Division done")
        else:
            logging.error("Invalid operator")
            return jsonify({"error": "Invalid operator"}), 400
        
        logging.info("Answer returned in JSON format")
        return jsonify({"Answer": result})
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


# Main function
if __name__ == '__main__':
    app.run(debug=False)  # Important for development!