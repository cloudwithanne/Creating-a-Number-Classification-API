from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    
    # Input validation
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400
    
    number = int(number)
    
    # Classify the number
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    # Get fun fact from Numbers API
    response = requests.get(f'http://numbersapi.com/{number}/math?json')
    fun_fact = response.json().get('text', 'No fun fact available.')
    
    # Prepare the response
    result = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": False,  # Placeholder, implement if needed
        "properties": properties,
        "digit_sum": digit_sum(number),
        "fun_fact": fun_fact
    }
    
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(debug=True)
