#!/usr/bin/env python3
import random
secret_number = random.randint(1, 10)
# guess = int(input("guess the number: "))
count = 0
while True:
    guess = int(input("guess the number: "))
    count += 1
    match guess:
        case _ if secret_number == guess:
            print("Congratulations, you guessed it")
            break
        case _ if guess > secret_number:
            print("Oops, your guess is a bit high. Try again!")
        case _ if guess < secret_number:
            print("Nope, your guess is a bit low. Give it another shot!")
print(f"the number of guess is: {count}")