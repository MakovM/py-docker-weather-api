import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
URL = "http://api.weatherapi.com/v1/current.json"
CITY = "Paris"


def get_weather() -> None:
    print(f"Weather API for city {CITY}...")

    response = requests.get(
        url=URL,
        params={
            "key": API_KEY,
            "q": CITY
        }
    )

    if response.status_code != 200:
        print(f"Error from API: {response.text}")

    data = response.json()
    location = data["location"]["name"]
    country = data["location"]["country"]
    localtime = data["location"]["localtime"]
    temp_c = data["current"]["temp_c"]
    condition = data["current"]["condition"]["text"]

    print(
        f"{location}/{country} {localtime} "
        f"Weather: {temp_c} Celsius, {condition}"
    )


if __name__ == "__main__":
    get_weather()
