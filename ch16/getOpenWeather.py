import sys, requests, json

if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name,2-letter_country_code")
    sys.exit()

location = sys.argv[1]
APPID = "9f3c154da217f1ba7f89c9b835ba0222"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {"q": location, "appid": APPID}

print("Making request to:", url)
print("With params:", params)

response = requests.get(url, params=params)
response.raise_for_status()

weatherData = response.json()

print(json.dumps(weatherData, indent=2))
