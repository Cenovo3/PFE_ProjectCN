import requests

def get_location(city_name, country=None, count=0):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": city_name,
        "count": count
    }
    if country:
        params["country"] = country
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    if "results" not in data or len(data["results"]) == 0:
        raise ValueError("No location found for the given city/country.")
    city_data = data["results"][0]
    return {
        "city": city_data.get("name"),
        "country": city_data.get("country"),
        "latitude": city_data.get("latitude"),
        "longitude": city_data.get("longitude")
    }
def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    weather_info = data.get("current_weather", {})
    return {
        "temperature": weather_info.get("temperature"),
        "windspeed": weather_info.get("windspeed"),
        "observation_time": weather_info.get("time"),
        "elevation": data.get("elevation")
    }
def main():
    city_name = input("Enter a city name: ").strip()
    country = input("Enter country: ").strip() or None
    try:
        location = get_location(city_name, country)
        weather = get_weather(location["latitude"], location["longitude"])
        city_weather = {
            "city": location["city"],
            "country": location["country"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "temperature": weather["temperature"],
            "windspeed": weather["windspeed"],
            "observation_time": weather["observation_time"],
            "elevation": weather["elevation"]
        }
        print("\n--- Weather Information ---")
        print(city_weather)
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()
