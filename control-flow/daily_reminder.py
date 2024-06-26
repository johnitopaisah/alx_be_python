#!/usr/bin/env python3
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == "yes":
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority task that requires immediate attention today!")
    case 'medium':
        if time_bound == 'yes':
            print(f"{task} is a {priority} priority task, but try to do this on time!")
        else:
            print(f"{task} is a {priority} priority task consider completing it when you have free time")
    case 'low':
        if time_bound == 'yes':
            print(f"{task} is a {priority} priority task, but try to do this on time!")
        else:
            print(f"{task} is a {priority} priority task consider completing it when you have free time")