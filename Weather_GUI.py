from tkinter import *
import time
# time module will be needed if we're communicating via txt files

def print_HW():
    print("Hello world!")

def find_weather_by_zipcode(zipcode):
    """
    Function for Tkinter search button.
    Should return following data from OpenWeather API:
        Location
        Temp (High / Low / Current)
        Description of conditions (Cloudy, Rainy, etc)
    :param zipcode:
    :return:
    """

root = Tk()
root.title("Weather App")

# Create a place for image to go
#canvas = Canvas(root, width=300, height=400)
#canvas.pack()

# Create a search bar
search_bar = Entry(root)
search_bar.pack()

# Create a button to execute search for string in search bar
button_text = "Search zipcode"
button = Button(root, width=30, text=button_text, command=print_HW)
button.pack()

# Create a button to exit the software
button_text = "Exit window"
button = Button(root, width=30, text=button_text, command=root.destroy)
button.pack()

root.mainloop()