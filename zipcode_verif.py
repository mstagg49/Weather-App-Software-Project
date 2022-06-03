import csv


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

