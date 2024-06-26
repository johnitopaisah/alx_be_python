def uppercase(str):
    new_str = ''
    for char in str:
        if 97 <= ord(char) <= 122:
            new_str = new_str + chr(ord(char) - 32)
        else:
            new_str = new_str + char
    print(new_str)

uppercase("best")
uppercase("Best School 98 Battery street")
