from city import City
from tkinter import *

def command_func():
    city_names = city_name_input.get()
    city = City(city_names)
    return city.find_lat_long()

window = Tk()
window.title("Weather")
window.config(padx=4, pady=4, bg="#82839E")

canvas = Canvas(width=500, height=250, highlightthickness=0, bg="#82839E")
image = PhotoImage(file="logo (2).png")
canvas.create_image(250, 125, image=image)
canvas.grid(column=0, row=0, columnspan=3)

info_lable = Label(text="Welcome to Open Weather Data app. You can find weather datas like temperature, "
                        "wind speed, humidity and etc.", pady=10, bg="#CCCDDC")
info_lable.grid(row=1, column=0, columnspan=3)
city_name_input = Entry(width=40)
city_name_input.grid(row=2, column=1, pady=15)
city_name_input.focus()

city_name = Label(text="City, Country:")
city_name.grid(column=0, row=2)

search_button = Button(text="Search", command=command_func)
search_button.grid(row=2, column=2)



window.mainloop()
