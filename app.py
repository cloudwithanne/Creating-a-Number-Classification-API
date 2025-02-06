from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    num_str = str(abs(n))  # Use absolute value for Armstrong check
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == abs(n)

def digit_sum(n):
    # Convert to string and remove the decimal point if it exists
    n_str = str(abs(n)).replace('.', '')
    return sum(int(digit) for digit in n_str)  # Use absolute value for digit sum

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    try:
        # Convert to float to accept negative and floating-point numbers
        number = float(number)
    except ValueError:
        return jsonify({"number": number, "error": True}), 400  # Return 400 for invalid input
    
    # Classify the number
    properties = []
    
    # Check if the number is an integer
    if number.is_integer():
        number_int = int(number)  # Convert to integer for further checks
        if is_armstrong(number_int):
            properties.append("armstrong")
        if is_prime(number_int):
            properties.append("prime")
    else:
        properties.append("not_integer")  # Indicate that it's not an integer

    # Check if the number is even or odd
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Get fun fact from Numbers API (only for integers)
    fun_fact = "No fun fact available."
    if number.is_integer():
        response = requests.get(f'http://numbersapi.com/{number_int}/math?json')
        if response.status_code == 200:
            fun_fact = response.json().get('text', 'No fun fact available.')
    
    # Prepare the response
    result = {
        "number": number,
        "is_prime": is_prime(number_int) if number.is_integer() else False,
        "is_perfect": False,  # Placeholder, implement if needed
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
    
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
