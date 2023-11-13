# Import necessary libraries
import uvicorn
import requests
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create a FastAPI app instance
app = FastAPI()

# Print a message to indicate that the FastAPI server is starting
print("Starting FastAPI server...")

# Define constants and set up headers for API requests
API_BASE_URL = "https://adsbexchange-com1.p.rapidapi.com"
PORT = 8000
API_KEY = os.getenv('API_KEY')

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "adsbexchange-com1.p.rapidapi.com"
}

# Define a FastAPI route to handle requests to "/tagged-aircrafts"
@app.get("/tagged-aircrafts")
def get_tagged_aircraft_data():
    # Create the URL for the API request
    url = f"{API_BASE_URL}/v2/mil/"
    
    # Make an HTTP GET request to the API with the specified headers
    response = requests.get(url, headers=headers)
    
    # Print the API request URL for debugging purposes
    print("Making API call to: ", url)

    # Check the HTTP response status code
    if response.status_code == 200:
        try:
            # Parse the JSON response data
            data = response.json()
            # Return a JSONResponse with the parsed data to view in browser
            return JSONResponse(content=data)
        except ValueError:
            # Handle the case where the response is not valid JSON
            print("Response is not valid JSON.")
    else:
        # Handle the case where the API request failed
        print(f"Request failed with status code: {response.status_code}")

# Define a FastAPI route to handle requests to "/27.943721/lon/-82.537932/dist/5/"
@app.get("/overhead-iex")
def get_overhead_iex_data():
    # Create the URL for the API request
    url = f"{API_BASE_URL}/v2/lat/27.943721/lon/-82.537932/dist/5/"

    # Print the API request URL for debugging purposes
    print("Making API call to: ", url)

    # Make an HTTP GET request to the API with the specified headers
    response = requests.get(url, headers=headers)

       # Check the HTTP response status code
    if response.status_code == 200:
        try:
            # Parse the JSON response data
            data = response.json()
            # Return a JSONResponse with the parsed data to view in browser
            return JSONResponse(content=data)
        except ValueError:
            # Handle the case where the response is not valid JSON
            print("Response is not valid JSON.")
    else:
        # Handle the case where the API request failed
        print(f"Request failed with status code: {response.status_code}")



# Run the FastAPI application using uvicorn
if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)