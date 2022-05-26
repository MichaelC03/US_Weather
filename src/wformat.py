def weather_to_str(city, data):
    text = f"# {city.upper().replace('_', ' ')}\n"

    # Formatting JSON to MD
    for period in data:
        text += f"## **{period['name']}**\n"
        text += f"*{period['detailedForecast']}*  \n"
        text += f"**Temperature**: {period['temperature']}{period['temperatureUnit']}  \n"
        text += f"**Wind Speed**: {period['windSpeed']}  \n  \n"

    return text


def str_to_md(text):
    # Writing to MD file
    with open("weather_forecast.md", "w") as write_file:
        write_file.write(text)
