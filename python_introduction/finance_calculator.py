#!/usr/bin/env python3

income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))

monthly_saving = income - expenses

projected_saving = int((monthly_saving * 12 + (monthly_saving * 12 * 0.05)))

print(f"Your monthly savings are {monthly_saving}.")
print(f"Projected savings after one year, with interest, is: {projected_saving}.")