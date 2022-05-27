import json
import requests
from geopy.geocoders import Nominatim


def get_forecast(city):
    """Returns the weather forecast of the next week for the specified US city,
    represented as a list of dictionaries
    """

    # Get latitude and longitude coordinates of city, and whether or not an
    # error occured while doing so
    lat, lon, city_error = get_city_coords(city)

    # If an error occured while getting latitude and longitude (ie. city does
    # not exist in the US), print an error message and exit the function
    if city_error:
        print(f"{city.upper().replace('_', ' ')} was not found in the US")
        return

    # Get URL containing gridpoints related to specified latitude and
    # longitude, and whether an error occured while doing so
    response, coords_error = query_coords(lat, lon)

    # If an error occured in query_coords (ie. invalid latitude and longitude),
    # print an error message. Otherwise, query the obtained gridpoints URL and
    # return the requested weather forecast
    if coords_error:
        print(
            f"Error {response['status']}\n{response['title']}\n{response['detail']}")
    else:
        return query_grid(response)


def get_city_coords(city):
    """Returns the latitude and longitude coordinates of a city located in the
    United States
    """

    # Find coordinates of city
    geolocator = Nominatim(user_agent="wquery")
    # Forces city to be recognized as a city name and limits search to US
    query = {"city": city}
    location = geolocator.geocode(query, country_codes="us")

    # Return city's latitude and longitude. If city was not found, set error
    # variable to true
    if location:
        return location.latitude, location.longitude, False
    else:
        return 0, 0, True


def query_coords(lat, lon):
    """Returns the API URL containing the gridpoints of the grid cell related
    to the specified latitude (lat) and longitude (lon)
    """

    # Querying URL using lat and lon coordinates
    points_url = "https://api.weather.gov/points/" + \
        str(lat) + "," + str(lon)
    response = requests.get(points_url)
    data = json.loads(response.text)

    # Return the requested URL. If an error occured (ie. invalid coordinates),
    # return the error data and set the error variable to true
    try:
        return data["properties"]["forecast"], False
    except:
        return data, True


def query_grid(url):
    """Returns a list of dictionaries representing the weather forecast of a
    certain grid cell in the US using the given URL
    """

    # Taking grid endpoints URL from data to retrieve weather forecast
    response = requests.get(url)
    data = json.loads(response.text)["properties"]["periods"]
    return data
