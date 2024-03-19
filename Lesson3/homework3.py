#calculator Tokmakova Anna
operation = '*'
num1 = 100
num2 = 50

if operation == '+':
    print(num1+num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 == 0:
        print("Division by 0")
    else:
        print(num1 / num2)
else:
    print("Undefined operation")
