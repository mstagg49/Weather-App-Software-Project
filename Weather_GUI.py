from tkinter import *
import time
from functools import partial


def find_weather_by_zipcode(zipcode):
    """
    Function for Tkinter search button.
    Should return following data from OpenWeather API:
        Location
        Temp (High / Low / Current)
        Description of conditions (Cloudy, Rainy, etc)
    """
    # Send zipcode to zipcode_verify.py
    txt_file = open('zipcode-verif-service.txt', 'w')
    txt_file.write(str(zipcode))  # Converts to String
    txt_file.close()

    # Wait for zipcode_verify.py to run
    time.sleep(5)

    # Read zipcode-verif-service.txt
    txt_file = open('zipcode-verif-service.txt', 'r')
    txt_file_content = txt_file.read()
    txt_file = open('zipcode-verif-service.txt', 'w')
    txt_file.close()  # open in write mode and then close to clear text from file (Necessary)

    # If False, write error message
    if txt_file_content == "False":
        false_label = Label(root, text='This is not a valid zipcode. Please enter a new zipcode.')
        false_label.pack()
        return

    # Else, get information for that zipcode!
    # write zipcode to API service txt
    txt_file = open('get-API-data-service.txt', 'w')
    txt_file.write(zipcode)
    txt_file.close()

    # Wait for Weather_API_Call.py to run
    time.sleep(5)

    # Pull data from API service txt (delimited by commas)
    txt_file = open('get-API-data-service.txt', 'r')
    weather_data = txt_file.read()
    txt_file = open('get-API-data-service.txt', 'w')    # open in write mode and then close to clear text from file (Necessary)
    txt_file.close()
    print(weather_data)

    # Separate data by delimiter (comma)
    # data order: temp, condition, location
    weather_data = weather_data.split(', ')

    temp_label = Label(root, text=weather_data[0])
    temp_label.pack()
    cond_label = Label(root, text=weather_data[1])
    cond_label.pack()
    loc_label = Label(root, text=weather_data[2])
    loc_label.pack()





root = Tk()
root.title("Weather App")

# Create a place for image to go
#canvas = Canvas(root, width=300, height=400)
#canvas.pack()

# Create a search bar
search_bar = Entry(root, borderwidth=5)
search_bar.pack()


# Create a button to execute search for string in search bar
button_text = "Search zipcode"
button = Button(root, width=30, text=button_text, command=lambda: find_weather_by_zipcode(search_bar.get()))
button.pack()

# Create a button to exit the software
button_text = "Exit window"
button = Button(root, width=30, text=button_text, command=root.destroy)
button.pack()

root.mainloop()