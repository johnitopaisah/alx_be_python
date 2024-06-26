#!/usr/bin/env python3
# To print in hexa, we can use the formatted string in
#  this form f'{value:x}' <== the 'x' simply specify 
#  we want the hexa format
for num in range(0, 99):
    print(f"{num} = 0x{num:X}")