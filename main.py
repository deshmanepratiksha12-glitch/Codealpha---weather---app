import requests

API_KEY = "YOUR_API_KEY_HERE"

def get_weather():
    city = input("Enter city name: ")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=15)

        if response.status_code == 200:
            data = response.json()

            print("\n--- Weather Report ---")
            print("City:", data["name"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Humidity:", data["main"]["humidity"], "%")
            print("Weather:", data["weather"][0]["description"].title())

        elif response.status_code == 401:
            print("API key is invalid or not activated yet.")

        elif response.status_code == 404:
            print("City not found. Please check the city name.")

        else:
            print("Unable to get weather data.")
            print("Status code:", response.status_code)

    except requests.exceptions.RequestException as error:
        print("Connection error:", error)

get_weather()