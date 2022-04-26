from tkinter import *
from PIL import ImageTk, Image
import time


def find_weather_by_zipcode(zipcode):
    """
    Function for Tkinter search button.
    Should return following data from OpenWeather API:
        Location
        Temp (High / Low / Current)
        Description of conditions (Cloudy, Rainy, etc)
    """
    global weather_img

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
        invalid_zip_text = 'This is not a valid zipcode. Please enter a new zipcode.'
        invalid_zip_label.config(text=invalid_zip_text)
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
    # data order: temp, condition, location, icon
    weather_data = weather_data.split(', ')

    # Display requested weather data
    icon_id = weather_data[3]
    # construct file path for Weather Icon
    icon_path = 'weather_icons\\' + str(icon_id) + '.jpg'
    # load image into window
    weather_img = ImageTk.PhotoImage(Image.open(icon_path))

    # Display data:
    # Note - putting the label creation outside the function made this work
    #   you're only configuring the label in the function, not creating a new one every time
    # Location
    loc_label.config(text=weather_data[2])
    # Weather Condition
    cond_label.config(text=weather_data[1])
    # Temperature
    c_temp = round((float(weather_data[0])-273.15) * (9/5) + 32)
    temp_label.config(text=str(c_temp) + ' F')
    # Icon
    icon_label.config(image=weather_img)

    # Display hyperlink



# Initializing Tkinter window
root = Tk()
root.geometry("300x300")
root.config(background="blue")
root.title("Weather App")

# Creating labels for data display
# Location
loc_label = Label(root)
loc_label.pack()
# Weather Condition
cond_label = Label(root)
cond_label.pack()
# Temperature
temp_label = Label(root)
temp_label.pack()
# Icon
icon_label = Label(root)
icon_label.pack()

# Frame for invalid zipcode
invalid_zip_label = Label(root)
invalid_zip_label.pack()

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

# Create label where hyperlink will go
hyperlink_label = Label(root)
hyperlink_label.pack()

root.mainloop()