# 1-------------------------------
# def say_hello():
#     print('Hello')
#
# say_hello()

# 2----------------------------------
# def say_hello(name):
#     print(f'Hello, {name}')
#
# user_name = input('Enter your name: ')
# say_hello(user_name)

# 3-----------------------------------
# def say_hello(names):
#     for name in names:
#         print(f'Hello, {name}')
# user_name= ['Anna', 'Ira', 'Maria']
# say_hello(user_name)

# 4-----------------------------------
# def say_hello(names):
#     for name in names:
#         print(f'Hello, {name.title()}')
# user_name= ['Anna', 'Ira', 'Maria']
# new = ['Test']
# say_hello(user_name)
# say_hello(new)

# 5------------------------------------
# def add_elements():
#     pass
#
# def divide():
#     pass

# 6-------------------------------------
# def greetings(name):
#     return f'Hello, {name}!'
#
# result = greetings('Maryna')
# print(result)

# 7---------------------------------------------
# def greetings(name, is_upper):
#     if is_upper:
#         name.upper()
#     return f'Hello, {name}!'
#
# result = greetings('Maryna', is_upper=True)
# print(result)

# 8------------------------------------------------
# def greetings(name: str, is_upper: bool) -> str:
#     if is_upper:
#         name.upper()
#     return f'Hello, {name}!'
#
# result = greetings('Maryna', True)
# print(result)

# 9------------------------------------------------
# languages = {'fr': 'Bonjour', 'en': 'Hello', 'ua': 'Привіт'}
# def greetings(name, language='en') -> str:
#     word = languages[language]
#     return f'{word}, {name}!'
#
# print(greetings(language='fr', name='Anna'))

# 10 ----------------------------------------------
# employees = ['Matyna']
# def add_employee(name: str, emp=[]):
#     return emp.append(name)
#
# add_employee('Ivan', employees)
# print(employees)

# 11-------------------------------------------------
# def add_employee(name: str, emp=None):
#     if emp is None:
#         emp = []
#     emp.append(name)
#     return emp
#
# developer = add_employee('Ivan')
# print(developer)
# accounter = add_employee('Olga')
# print(accounter)

# 12--------------------------------------------------------
# LEGB
# scope = 'global'
#
# def outer():
#     scope = 'enclosed'
#
#     def inner():
#         scope = 'local'
#         print(scope)
#
#     inner()
# outer()

# 13------------------------------------------------------
# counter = 0
# def increment() -> int:
#     return counter + 1
#
# print(increment())

#----------------------------------------------
import math

def is_prime(number: int) -> bool:
    if number < 2 or number > 1000:
        print('This number does not belong to the necessary interval of numbers')
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

number = int(input('Enter number for checking from 2 to 1000: '))
if is_prime(number):
    print(f'{number} is prime')
else:
    print(f'{number} is not prime')