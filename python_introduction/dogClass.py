#!/usr/bin/env python3

from datetime import datetime


class Dog:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = datetime.strptime(birthday, "%m/%d/%Y")
        self.attendance = 0

    def age(self):
        today = datetime.today()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))


# Object of one individual dog
rufus = Dog(name="Rufus", birthday="2/1/2017")

# Object of individual dog
fluffy = Dog(name="Fluffy", birthday="1/12/2019")

# Print their details
print(f"Name: {rufus.name}, Age:  {rufus.age()}, Attendance: {rufus.attendance}")
print(f"Name: {fluffy.name}, Age: {fluffy.age()}, Attendance: {fluffy.attendance}")