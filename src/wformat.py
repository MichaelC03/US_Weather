def weather_to_str(city, data):
    """Formats weather forecast as a markdown file and saves it to a string"""

    text = f"# {city.upper().replace('_', ' ')}\n"

    # Formatting JSON to MD
    for period in data:
        text += f"## **{period['name']}**\n"
        text += f"*{period['detailedForecast']}*  \n"
        text += f"**Temperature**: {period['temperature']}{period['temperatureUnit']}  \n"
        text += f"**Wind Speed**: {period['windSpeed']}  \n  \n"

    return text


def str_to_md(text, title):
    """Write text string to a markdown file with the specified title"""

    # Writing to MD file
    with open(f"{title}.md", "w") as write_file:
        write_file.write(text)
