from flask import Flask, jsonify 
import requests
from dotenv import load_dotenv
import os

load_dotenv() #loaded environment variables from .env file

app = Flask(__name__)

print("Starting Flask server...")


# Base URl
API_BASE_URL = "https://adsbexchange-com1.p.rapidapi.com"
PORT = 8000
API_KEY = os.getenv('API_KEY')

headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
}

# Accept a registration number as a variable part of the URL
@app.route('/registration/<reg>') # http://127.0.0.1:8000/registration/ "required reg number"
def get_aircraft_data(reg):
    # Use the passed registration number in the URL
    url = f"{API_BASE_URL}/v2/registration/{reg}/"
    response = requests.get(url, headers=headers)
    # Return the response using jsonify
    print("Making API call to: ", url)
    return jsonify(response.json())

@app.route("/tagged-aircrafts") # http://127.0.0.1:8000/tagged-aircrafts
def get_tagged_aircraft_data():
    url = f"{API_BASE_URL}/v2/mil/"
    response = requests.get(url, headers=headers)
    print("Making API call to: ", url) 
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "API call failed"}), response.status_code

if __name__ == '__main__': 
    app.run(host="0.0.0.0", port=8000)