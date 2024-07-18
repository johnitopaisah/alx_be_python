#!/usr/bin/env python3

def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiple':
        return num1 * num2
    if operation == 'divide':
        if num2 == 0:
            return f'Cannot divide by zero'
        else:
            return num1 / num2
    else:
        return f'Invalide operation'