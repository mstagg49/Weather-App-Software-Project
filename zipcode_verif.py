import csv
import time


def zipcode_binary_search(array, zipcode):
    """
    Searches a list of zipcodes for the user entry. If not available, returns error message.
    Communicates with other Python files via .txt files
    """
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if array[mid] == zipcode:   # means x is present at mid
            return True
        if array[mid] < zipcode:  # If x is greater, ignore left half
            low = mid + 1
        elif array[mid] > zipcode:  # If x is smaller, ignore right half
            high = mid - 1

    return False  # If we reach here, then the element was not present


def generate_zip_list(csv_file, output):
    """
    Generates a list of valid zipcodes from CSV file containing detailed US zipcode information.
    """

    valid_zips = output
    with open(csv_file, "r", newline="") as file:
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            valid_zips.append(row[0])
    valid_zips.pop(0)


while True:
    time.sleep(1)
    # Open, read, store data, close (txt file)
    txt_file = open('zipcode-verif-service.txt', 'r')
    user_zipcode = txt_file.read()
    if user_zipcode != "":
        txt_file.close()
        valid_zipcodes = []
        generate_zip_list('uszips.csv', valid_zipcodes) #string data type
        verif_result = zipcode_binary_search(valid_zipcodes, str(user_zipcode)) # Returns Bool
        txt_file = open('zipcode-verif-service.txt', 'w')
        txt_file.write(str(verif_result))   # Converts Bool to String
        txt_file.close()
        time.sleep(5)
