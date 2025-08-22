# OPEN_WEATHER
Weather API for cities across the U.S.
Features: This script gives the temperature, humidity, feels like temperature, daily minimum temperature, daily maximum temperature and a description of the weather.
get_weather.py/
│── .env/           # Source files
│── .gitignore/     # Ignored files
│── get_weather.py/ # City Weather Script
│── README.md       # Project info

This script uses Python 3.11.9 and requires the following libraries
1. requests
2. os
3. dotenv
4. streamlit
5. streamlit_chat

Steps to run script
1. Open the driectiory in VS Code
2. Run "python -m venv venv" to creat a virtual environment
3. Run ".\venv\Scripts\Activate.ps1" to activate your virtual environment
4. Run "pip install -r requirements.txt" to install all the modules in your virtual environment (make sure you are actually in that OPEN_WEATHER Directory)
5. You can check to make sure you have the proper libraries installed using "pip list"
6. Go to get weather.py and run "streamlit run c:your/file/directory" (for me it was "streamlit run c:/Users/Micha/Documents/Duke_Classes/AIPI_503/OPEN_WEATHER/get_weather.py")
7. Enjoy!
8. Once you have the script running, it asks you for the city that you would like the weather for.
