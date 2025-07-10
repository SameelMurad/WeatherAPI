import pandas as pd
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

city_name = "Birmingham"
country_code = "UK"

def get_weather(city_name, country_code):
    configure()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={os.getenv('API_key')}"
    
    response = requests.get(url).json()
    
    weather_data = {
        'timestamp': datetime.now(),
        'city': response['name'],
        'country': response['sys']['country'],
        'temperature': response['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
        'feels_like': response['main']['feels_like'] - 273.15,
        'humidity': response['main']['humidity'],
        'description': response['weather'][0]['description'],
        'wind_speed': response['wind']['speed']
    }
    
    return weather_data

def save_weather_data(weather_data, filename='weather_data.csv'):
    df = pd.DataFrame([weather_data])
    
    import os
    file_exists = os.path.isfile(filename)
    
    df.to_csv(filename, mode='a', header=not file_exists, index=False)
    print(f"Data saved to {filename}")

# Call the function
result = get_weather(city_name, country_code)
if result:
     save_weather_data(result)


# Collect data every hour for testing
while True:
    result = get_weather(city_name, country_code)
    if result:
        save_weather_data(result)
    time.sleep(3600)