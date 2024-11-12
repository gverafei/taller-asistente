import requests
from os import getenv

def get_weather(city):
    weather_key = getenv("WEATHER_API_KEY")
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={weather_key}&q={city}&aqi=no")
    if response.status_code == 200:
        result = {}
        result["temperatura"] = str(response.json()["current"]["temp_c"]) + " grados celsius"
        result["condicion"] = response.json()["current"]["condition"]["text"]
        return result
    else:
        print(f"Hubo un error con el código: {response.status_code}")