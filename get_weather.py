import requests
import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_chat import message
import regex as re

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
    return(f"In {city_name}, the low is {temp_min}°C and the max is {temp_max}°C. It is {temp}°C with {description} although it feels like {feels_like}°C. The humidity is {humidity}.")

#Now incorporating this with Streamlit and input on there from the user
# Initialize a session state list to hold the conversation
if "history" not in st.session_state:
    st.session_state.history = []

st.header("Weather App")
st.markdown("Please enter the city you would like the weather for below:")
# 1. Capture user input
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("Please enter the city you would like the weather for below:", key="input", label_visibility="collapsed")
with col2:
    submit_button = st.button("Get Weather")

if not user_input:
    st.stop()
        
# 2. Run when user presses Enter OR button
if user_input or st.button("Get Weather"):
    # Get weather
    bot_response = get_weather(user_input)

    # Save chat
    st.session_state.history.append({
        "user": user_input,
        "bot": bot_response
    })

    # Clear input box
    st.session_state.city_input = ""

# 3. Display the chat history
for i, chat in enumerate(st.session_state.history):
    message(chat["user"], is_user=True, key=f"user_{i}")
    message(chat["bot"],     key=f"bot_{i}")
