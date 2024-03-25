num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
operation = (input('Enter operation (+, -, *, /): '))

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = 'Division by 0'
    else:
        result = num1 / num2
else:
    result = 'Undefined operation'

print(f'\tResuilt of {operation} is {result} ')
