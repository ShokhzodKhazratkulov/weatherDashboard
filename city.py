import requests
from weather_data import WeatherData


class City:

    def __init__(self, name):
        self.url = "https://api.opencagedata.com/geocode/v1/json"
        self.api_key = "YourApiKey"
        self.query = name

    def find_lat_long(self):
        params = {
            "key": self.api_key,
            "q": self.query
        }
        response = requests.get(self.url, params=params)
        response.raise_for_status()
        lat_lng_data = response.json()

        city_lat = lat_lng_data["results"][0]["geometry"]["lat"]
        city_lng = lat_lng_data["results"][0]["geometry"]["lng"]

        weather_data = WeatherData(city_lat, city_lng)
        return weather_data.display_weather_data()


