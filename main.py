from tkinter import *
import requests

from Json_query import functionQueryJSON as wJ


def showWeatherFunction(weatherR):
	try:
		nameCity =  weatherR["name"]
		desc = weatherR["weather"][0]["description"]
		temp = weatherR["main"]["temp"]
		min_rangeT = weatherR["main"]["temp_min"]
		max_rangeT = weatherR["main"]["temp_max"]
		p_humidity = weatherR["main"]["humidity"]

		showCity["text"] = nameCity
		estate_clime["text"] = str(float(temp)) + "°C"		
		descriptionWeather["text"] =  desc
		range_temp["text"] = str(float(min_rangeT)) + "°C Min" + " " + str(float(max_rangeT)) + "°C Max"
		humidity_show["text"] = "Humedad: " +  str(float(p_humidity)) + "%"

	except:
		showCity["text"] = ":( Datos no disponibles."


#ver, mejorar
windows = Tk()
windows.geometry("350x550")

input_City = Entry(windows, font = ("Segoe UI", 20, "normal"), justify = "center", bg="white", relief = "ridge", bd="1")
input_City.pack(padx =  30, pady = 20)

show_weather = Button(bg="white", relief = "ridge", bd="1", font = ("Segoe UI", 10, "normal"), text = "Obtener estado meteorológico", command = lambda: wJ(input_City.get()))
show_weather.pack()


showCity = Label(font = ("Segoe UI", 20, "normal"))
showCity.pack(padx =  20, pady = 20)

estate_clime = Label(font = ("Segoe UI", 50, "normal"))
estate_clime.pack(padx =  10, pady = 10)

descriptionWeather = Label(font = ("Segoe UI", 20, "normal"))
descriptionWeather.pack(padx =  10, pady = 10)

range_temp = Label(font = ("Segoe UI", 15, "normal"))
range_temp.pack(padx = 10, pady = 10)

humidity_show = Label(font = ("Segoe UI", 15, "normal"))
humidity_show.pack(padx = 10, pady = 10)

windows.mainloop()