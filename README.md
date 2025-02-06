# Creating-a-Number-Classification-API

This is a simple Flask API that classifies numbers and provides interesting mathematical properties about them, along with a fun fact.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Usage](#usage)

## Features

- Classifies numbers as prime, perfect, Armstrong, odd, or even.
- Returns the sum of the digits of the number.
- Provides a fun fact about the number using the Numbers API.

## Technologies Used

- Python 3.12
- Flask
- AWS EC2
- Git
- Virtual Environment

## Getting Started

### Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- Git

## API Endpoints
Classify Number
- Endpoint: `/api/classify-number`

- Method: `GET`

- Query Parameters:
   `number:` The number to classify (must be a valid integer).
Example Request:

```
curl "http://<your-ec2-public-ip>:8000/api/classify-number?number=371"
```

Success Response (200 OK):

```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number"
}
```

Error Response (400 Bad Request):

```
{
    "number": "alphabet",
    "error": true
}
```

## Deployment

This application is deployed on AWS EC2. The following steps were taken to deploy the application:

1. Launched an EC2 instance with Ubuntu Server 24.04 LTS, and connected via EC2 instance connect.

2. Update and install required packages:

```
sudo apt update
sudo apt install python3-pip -y
sudo apt install python3.12-venv -y
```

3. Clone the repository and set up the environment:
```
git clone https://github.com/yourusername/your-repo.git
cd your-repo
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run the Flask application:
```
flask run --host=0.0.0.0 --port=8000
```

5. Ensure port 8000 is open in your security group settings.

## Usage

To use the API, send a GET request to the `/api/classify-number` endpoint with a valid number as a query parameter. You can use tools like Postman or curl to test the API.
