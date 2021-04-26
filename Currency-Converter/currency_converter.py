# base currency = INR

USD = float(74.72) # United States Dollar
EUR = float(90.43) # Euro
JPY = float(0.69) # Japanese Yen
GBP = float(104.01) # Great Britain Pound
CAD = float(59.97) # Canadian Dollars

# from x to INR = *
# from INR to x = /

# inputs:
currency = input("Enter currency (USD, EUR, JPY, GBP, CAD): ")
from_to = input(f"Do you want to convert from {currency} to INR or from INR to {currency} (1, 2)? ")
amount = float(input("Enter the amount: "))

result = None # None is a data type, it holds nothing

if from_to == "1": # from x to INR
    if currency == "USD":
        result = amount * USD
    if currency == "EUR":
        result = amount * EUR
    if currency == "JPY":
        result = amount * JPY
    if currency == "GBP":
        result = amount * GBP
    if currency == "CAD":
        result = amount * CAD

    if result is None:
        print("Invalid currency")
    else:
        print(f"{amount} {currency} = {result} INR") # 10 x = 20 INR

elif from_to == "2": # from INR to x
    if currency == "USD":
        result = amount / USD
    if currency == "EUR":
        result = amount / EUR
    if currency == "JPY":
        result = amount / JPY
    if currency == "GBP":
        result = amount / GBP
    if currency == "CAD":
        result = amount / CAD

    if result is None:
        print("Invalid currency")
    else:
        print(f"{amount} INR = {result} {currency}") # 10 INR = 20 x

else:
    print("Invalid choice")
