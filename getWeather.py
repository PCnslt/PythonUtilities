from dotenv import load_dotenv
import os, requests

LATITUDE = 38.693115
LONGITUDE = -77.316084
CITY = 'Washington'

def get_weather_lat_lon(lat, lon):
    """Get the 5day/3hr forecast by lat and lon"""
    load_dotenv('.secrets')
    appid = os.getenv('OPENWEATHERMAP_ORG_KEY')
    openweathermap_org_url = (f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={appid}&units=metric')
    weather_forecast = requests.get(openweathermap_org_url, timeout=300)
    return weather_forecast.json()

def get_weather_city(city):
    """Get the 5day/3hr forecast by city name
        Returns: 1) generates data.txt file with dateTimeHr, temperature, description
                 2) Result in output.
    """
    load_dotenv('.secrets')
    appid = os.getenv('OPENWEATHERMAP_ORG_KEY')
    openweathermap_org_url = (f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={appid}&units=metric')
    weather_forecast = requests.get(openweathermap_org_url, timeout=300)
    content = weather_forecast.json()
     
    result = []
    with open('data.txt','a') as city_weater_file:
        for dicty in content['list']:
            city_weater_file.write(f"{dicty['dt_txt']}, {dicty['main']['temp']}, {dicty['weather'][0]['description']}\n")
            result.append({"Time":dicty['dt_txt'], "Temperature":dicty['main']['temp'], "Description":dicty['weather'][0]['description']})
    
    return result


tomorrows_weather = get_weather_lat_lon(LATITUDE,LONGITUDE)
city_weather = get_weather_city(city=CITY)

# print(f"Weather based by lat/lon: {tomorrows_weather}")
# print(f"Weather forecast by city: {city_weather}")