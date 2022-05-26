import json
import requests
from geopy.geocoders import Nominatim


def get_forecast(city):
    lat, lon, city_error = get_city_coords(city)

    if city_error:
        print(f"{city.upper().replace('_', ' ')} was not found in the US")
        return

    response, coords_error = query_coords(lat, lon)

    if coords_error:
        print(
            f"Error {response['status']}\n{response['title']}\n{response['detail']}")
    else:
        return query_grid(response)


def query_coords(lat, lon):
    # Querying URL using coordinates
    points_url = "https://api.weather.gov/points/" + \
        str(lat) + "," + str(lon)
    response = requests.get(points_url)
    data = json.loads(response.text)

    try:
        return data["properties"]["forecast"], False
    except:
        return data, True


def query_grid(url):
    # Taking grid endpoints URL from data to retrieve weather info
    response = requests.get(url)
    data = json.loads(response.text)["properties"]["periods"]
    return data


def get_city_coords(user_city):
    geolocator = Nominatim(user_agent="wquery")
    query = {"city": user_city}
    location = geolocator.geocode(query, country_codes="us")

    if location:
        return location.latitude, location.longitude, False
    else:
        return 0, 0, True
