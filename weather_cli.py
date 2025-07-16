  import requests
import argparse

# Replace with your own OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city: str):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        temp = data["main"]["temp"]
        weather_desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n📍 Weather in {city_name}:")
        print(f"🌡️ Temperature: {temp}°C")
        print(f"🌤️ Condition: {weather_desc.capitalize()}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s\n")

    except requests.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.RequestException as err:
        print(f"❌ Request error: {err}")
    except KeyError:
        print("❌ Could not parse weather data. Please check the city name.")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI Weather App")
    parser.add_argument("city", help="City name to fetch the weather for")
    args = parser.parse_args()

    get_weather(args.city)

if __name__ == "__main__":
    main()
