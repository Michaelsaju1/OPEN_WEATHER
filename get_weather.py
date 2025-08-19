import requests
import os
from dotenv import load_dotenv

# Load your API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(city):
    """
    Fetch weather for the given city and print it nicely.
    """
    # 1. Create the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    # 2. Set query parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # temperature in Celsius
    }
    
    # 3. Make the request
    response = requests.get(url, params=params)
    
    # 4. Parse JSON
    data = response.json()
    
    # 5. Extract key info
    city_name = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]
    temp_min = data["main"]["temp_min"]
    temp_max = data["main"]["temp_max"]
    description = data["weather"][0]["description"]
    
    # 6. Print
    print(f"In {city_name}, the low is {temp_min}°C and the max is {temp_max}°C. It is {temp}°C with {description} although it feels like {feels_like}°C. The humidity is {humidity}.")

#Take in user input for City.
print("Please enter your the city name that you would like the weather for: ")
city = input()

# Try it with Raleigh
try: 
    get_weather(city)
except:
    print("Sorry! That is not a valid city. Please try again.")

#Check if there is any other city they want to check
print("Are there any other cities you would like to check the weather for? If so, please enter it here: ")
city = input()
get_weather(city)