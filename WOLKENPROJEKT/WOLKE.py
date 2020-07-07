import tkinter as tk
from tkinter import font
import requests


HEIGHT= 700
WIDTH = 800

def test_funktion(entry):
    print(entry)

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]['description']
        temp = weather["main"]['temp']

        final_str = "Stadt: %s \nWetterbedingungen: %s \nTemparatur : %s " "°C" % (name, desc, temp)


    except:
        final_str = "Es gab ein Problem"


    return final_str
def get_weather(city):
    weather_key = "64d544c1d670146d2ad146d6c8154f72"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()
    print(response.json())

    label["text"] = format_response(weather)


    

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width= WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file = r"C:\Users\Admin\Desktop\INDEX\WOLKENPROJEKT\ABC.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)



frame = tk.Frame(root, bg="#99004d", bd= 5)
frame.place(relx=0.5, rely=0.1, relwidth= 0.75, relheight=0.1, anchor = "n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Los", font= 10, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#99004d", bd=10 )
lower_frame.place(relx=0.5, rely=0.25,relwidth=0.75, relheight=0.6, anchor= "n")

label = tk.Label(lower_frame,fg="#2E2E2E",font=("Mikado Ultra", 15), anchor = "nw", justify= "left", bd=4 )
label.place(relwidth=1, relheight=1)








root.mainloop()