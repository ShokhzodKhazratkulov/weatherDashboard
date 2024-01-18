import requests


class WeatherData:

    def __init__(self, city_lat, city_lng):
        self.API_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
        self.API_KEY = "YourApi"
        self.MY_LAT = city_lat
        self.MY_LONG = city_lng

    def display_weather_data(self):
        parameters = {
            "lat": self.MY_LAT,
            "lon": self.MY_LONG,
            "appid": self.API_KEY,
            "cnt": 4,
        }

        response = requests.get(self.API_Endpoint, params=parameters)
        response.raise_for_status()
        data = response.json()

        rain_check = data["list"][0]["weather"][0]["id"]
        temp_check = data["list"][0]["main"]["temp"]
        humidity_check = data["list"][0]["main"]["humidity"]
        wind_speed_check = data["list"][0]["wind"]["speed"]

        temp = round(temp_check - 273.15)
        will_rain = False
        if rain_check > 700:
            will_rain = True

        print(f"Rain: {will_rain}\nTemp: {temp}°C\nHumidity: {humidity_check}%\nWind speed: {wind_speed_check}m/s")
