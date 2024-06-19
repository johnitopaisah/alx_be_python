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
    
    def bark(self):
        return f"{self.name} says: Woof!"

class HardingDog(Dog):
    def herd(self):
        return f"{self.name} is herding!"

class TrackingDog(Dog):
    def track(self):
        return f"{self.name} is tracking"
    

# Object of one individual dog
rufus = Dog(name="Rufus", birthday="2/1/2017")
fluffy = HardingDog(name="Fluffy", birthday="1/12/2019")
maisel = HardingDog(name="Maisel", birthday="3/5/2018")
duke = TrackingDog(name="Duke", birthday="6/8/2020")

# Print their details
print(f"Name: {rufus.name}, Age:  {rufus.age()}, Attendance: {rufus.attendance}")
print(f"Name: {fluffy.name}, Age: {fluffy.age()}, Attendance: {fluffy.attendance}")
print(f"Name: {maisel.name}, Age: {maisel.age()}, Attendance: {maisel.attendance}")
print(f"Name: {duke.name}, Age: {duke.age()}, Attendance: {duke.attendance}")
