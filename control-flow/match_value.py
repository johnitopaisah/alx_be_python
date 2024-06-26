value = input("Enter a value (number or string): ")

try:
    int_value = int(value)
    value_type = "int"
except ValueError:
    value_type = "str"

match value_type:
    case "int":
        print("You entered an integer:", value)
    case "str":
        print("You entered a string:", value)
    case _:
        print("Invalid data type entered.")