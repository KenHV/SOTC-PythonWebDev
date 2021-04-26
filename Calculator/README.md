# Calculator:

- Get two numbers from user
- Get desired operation to be performed
- Do the calculation
- Print the result

We can split this into smaller parts.

1. Add two numbers and print the result.

2. Get two numbers from user.

3. Get the operator from user.

## Part 1:

```
num_1 = 5
num_2 = 10
result = num_1 + num_2
print(result)
```

## Part 2:

```
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
result = num_1 + num_2
print("The result is:", result)
```

## Part 3:

```
num_1 = int(input("Enter 1st number: "))
num_2 = int(input("Enter 2nd number: "))
operator = input("Enter an operator: ")

if operator == "+":
    result = num_1 + num_2

if operator == "-":
    result = num_1 - num_2

if operator == "*":
    result = num_1 * num_2

if operator == "/":
    result = num_1 / num_2

print("The result is:", result)
```
