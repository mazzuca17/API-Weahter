import requests
import main


def functionQueryJSON(city):
	API_key =  "**************************************"
	URL = "https://api.openweathermap.org/data/2.5/weather"
	parametr = {"APPID": API_key, "q": city, "units": "metric", "lang": "es"}
	respones = requests.get(URL, params = parametr)
	weatherR = respones.json()
	#print(respones.json())

	print(weatherR["name"])
	print(weatherR["weather"][0]["description"])
	print(weatherR["main"]["temp"] ) 
	
	print(weatherR["main"]["temp_min"])
	print(weatherR["main"]["temp_max"])
	print(weatherR["main"]["humidity"]) 
	

	main.showWeatherFunction(weatherR)
