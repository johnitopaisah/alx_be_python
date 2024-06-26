#!/usr/bin/env python3

# Want to print value from 0 -> 99 and all the number
# printed must be 2-digits
# use 2 print() ==> How

for num in range(0, 100):
    if num < 10:
        print(f'0{num}', end=', ')
    # elif num == 99:
    #     print(num)
    else:
        print(num, end=', ' if num != 99 else '\n')