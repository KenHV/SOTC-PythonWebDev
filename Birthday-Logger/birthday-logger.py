from datetime import datetime
import json

print("Birthday Logger\n")
print("1. Add data")
print("2. Print data")
choice = int(input("Enter your choice: (1, 2) "))

# Dictionaries: Key-Value pairs
with open("birthdays.json", "r") as file:
    data = json.load(file)

if choice == 1:  # Add data
    name = input("Enter the name: ")
    date = input("Enter the date in DD/MM format: ")
    data[name] = date
    with open("birthdays.json", "w") as file:
        json.dump(data, file, indent=4)


def sort_dict_by_date(key):
    date = data.get(key)
    date_obj = datetime.strptime(date, "%d/%m")
    return date_obj


if choice == 2:
    sorted_data = sorted(data, key=sort_dict_by_date)
    print("\nBirthday Log:")
    for element in sorted_data:
        date = data.get(element)
        print(f"{element}\t{date}")








