#!/usr/bin/env python3

def getInteger():
    result = int(input("Entr integer: "))
    return  result

def Main():
    print("Started")

    # calling the getInteger funtion and
    # storting its returned value in the output varriable
    output = getInteger()
    print(output)

    # now we are required to tell Python 
    # for 'Main' returned value in the output varriable
    if __name__ == "__main__":
        Main()