#!/usr/bin/env python3

# for alp in range(ord('a'), (ord('z')+1)):
#     print(chr(alp), end='')

# print()

for alp in range(ord('a'), ord('z')+1):
    if chr(alp) == 'e' or chr(alp) == 'q':
        continue
    print(chr(alp), end=' ')


