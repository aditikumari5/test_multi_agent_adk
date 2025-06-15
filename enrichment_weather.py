import requests

class WeatherAgent:
    def run(self, context):
        # Use dummy coordinates if not found
        lat, lon = context.get("lat", 28.5), context.get("lon", -80.6)
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={context["weather_key"]}'
        resp = requests.get(url).json()
        return {
            "weather": resp["weather"][0]["description"],
            "temp": resp["main"]["temp"]
        }
