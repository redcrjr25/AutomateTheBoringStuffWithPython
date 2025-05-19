import sys, requests, json

if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name,2-letter_country_code")
    sys.exit()

location = sys.argv[1]
APPID = "1017e9154bbf1417b440db46b410de3a"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {"q": location, "appid": APPID, "units": "imperial"}

print("Making request to:", url)
print("With params:", params)

response = requests.get(url, params=params)
response.raise_for_status()

weatherData = response.json()

print(json.dumps(weatherData, indent=2))
