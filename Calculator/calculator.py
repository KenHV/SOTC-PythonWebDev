num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = None

if operator == "+":
    result = num_1 + num_2

elif operator == "-":
    result = num_1 - num_2

elif operator == "*":
    result = num_1 * num_2

elif operator == "/":
    result = num_1 / num_2

if result is None:
    print("Invalid operator!")
else:
    print("The result is: ", result)
