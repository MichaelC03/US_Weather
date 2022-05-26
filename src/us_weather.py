import argparse
import wquery
import wformat

# Setting up parser
my_parser = argparse.ArgumentParser(
    description="Obtain weather forecast of an area in the US")

# Latitude
my_parser.add_argument("city",
                       metavar="city",
                       type=str,
                       help="Enter a city located in the US")

# Parsing and saving user arguments
args = my_parser.parse_args()
city = args.city

data = wquery.get_forecast(city)

if data:
    text = wformat.weather_to_str(city, data)
    wformat.str_to_md(text)

    print("Success")
