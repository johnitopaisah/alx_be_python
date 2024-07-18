#!/usr/bin/env python3

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date_formated = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date_formated}")
    return current_date

def calculate_future_date():
    current_date = display_current_datetime()
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    time_delta = timedelta(days=days_to_add)
    future_date = current_date + time_delta
    future_date_formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future date: {future_date_formatted}")
    return future_date


if __name__ == "__main__":
    calculate_future_date()
