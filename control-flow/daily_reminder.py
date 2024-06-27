#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = "Invalid priority entered. Please enter 'high', 'medium', or 'low'."

match priority:
    case 'high':
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high priority task that requires immediate attention today!")
    case 'medium':
        if time_bound == 'yes':
            print(f"{task} is a medium priority task, but try to do this on time!")
        else:
            print(f"{task} is a medium priority task. Consider completing it when you have free time.")
    case 'low':
        if time_bound == 'yes':
            print(f"{task} is a low priority task, but try to do this on time!")
        else:
            print(f"{task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Reminder", reminder)