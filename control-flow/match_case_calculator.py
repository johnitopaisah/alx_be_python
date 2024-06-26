#!/usr/bin/python3

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operate = input("Choose the operation (+, -, *, /): ")

match operate:
    case '+':
        print(f"The result is {num1 + num2}")
    case '-':
        print(f"The result is {num1 - num2}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        print(f"The result is {num1 / num2}")
    case '*':
        print(f"The result is {num1 * num2}")
    case _:
        print("Not a valid operator")