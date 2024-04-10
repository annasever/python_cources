num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = (input('Enter operation (+, -, *, /): '))

def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2

def deduct_numbers(num1: int, num2: int) -> int:
    return num1 - num2

def multiply_numbers(num1: int, num2: int) -> int:
    return num1 * num2

def divide_numbers(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ZeroDivisionError('Division by zero is not allowed')
    return num1 / num2

def calculate_numbers(num1, num2, operation):
    if operation == '+':
        result = add_numbers(num1, num2)
    elif operation == '-':
        result = deduct_numbers(num1, num2)
    elif operation == '*':
        result = multiply_numbers(num1, num2)
    elif operation == '/':
        result = divide_numbers(num1, num2)
    else:
        raise ValueError('Undefined operation')
    return result

try:
    result = calculate_numbers(num1, num2, operation)
    print(f'Result of {num1} {operation} {num2} is {result}')
except (ZeroDivisionError, ValueError) as e:
    print(e)
