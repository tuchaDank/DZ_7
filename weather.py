import requests

import os


URL_API = "https://api.openweathermap.org/data/2.5/weather"


city = input("Введите название города, чтобы узнать погоду в нём: ")
api_key = os.getenv("OPENWEATHER_API_KEY")


params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "ru",
}

response = requests.get(URL_API, params=params, timeout=10)
response.raise_for_status()

weather = response.json()

temperature = weather["main"]["temp"]
description = weather["weather"][0]["description"]

print(f"Температура в городе {city}: {temperature} C, погода: {description}")
