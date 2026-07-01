import requests

def get_weather(city, api_key):
    # OpenWeatherMap API URL
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the request
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            print(f"\n--- Weather in {city.capitalize()} ---")
            print(f"Temperature: {main['temp']}°C")
            print(f"Condition: {weather['description'].capitalize()}")
            print(f"Humidity: {main['humidity']}%")
        else:
            print(f"Error: {data.get('message', 'City not found.')}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
API_KEY = "c2fae48ab0c18bfde6d78d8de64980d4"
city_name = input("Enter city name: ")
get_weather(city_name, API_KEY)