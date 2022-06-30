from cProfile import label
from multiprocessing import Condition
import tkinter as tk
from tkinter.font import BOLD
from pyparsing import condition_as_parse_action
import requests
import time
from validators import Min
from tkinter import *

def getWeather(canvas):
    city =textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=1a510f55c623b0c29e3ede4d543a599f"
    json_data = requests.get(api).json()
    condition= json_data['weather'][0]['main']
    temp=int(json_data['main']['temp']-273.15)
    min_temp=int(json_data['main']['temp_min']-273.15)
    max_temp=int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity= json_data['main']['humidity']
    wind = json_data['wind']['speed']

    final_info=condition + "\n" + str(temp) + "°c"
    final_data ="\n" + "Max Temp:" + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind speed : " + str(wind)
    label1.config(text = final_info)
    label2.config(text= final_data)

canvas= tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather Forecast App")

f = ("poppins", 15,"bold")
t = ("poppins", 35,"bold")

textfield = tk.Entry(canvas , font=t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)
label1= tk.Label(canvas, font = t)
label1.pack()
label2=tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()


