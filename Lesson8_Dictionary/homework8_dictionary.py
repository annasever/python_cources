# Task 1
print('Task 1: \'Roles and Users\'')
roles = {
    'admin': ['Olga', 'Julia'],
    'maintainer': ['Oleg', 'Roman'],
    'manager': ['Ruslan', 'Artem'],
    'developer': ['Viktor', 'Alex']
}

name = input('Please to enter name with upper registr for first letter: ')
role = []
for key, value in roles.items():
    if name in value:
        role = key
        break
if role:
    print(f'Hello, {role}')
else:
    print('Hello, Guest')

# Task 2
print('\nTask 2: \'Formatted link\'')
# result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
result_str = ''

for key, value in params.items():
    result_str += f'{key}={value}&'
result_str = result_str.rstrip('& ')
result_link = initial_str + result_str
print(f'After formatting the string and dictionary, we get this link: {result_link}')

# Task 3
print('\nTask 3: \'Creating dictionary\'')
print('1 way: With Counter')
result_link1 = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
from collections import Counter
result_dict = Counter(result_link1)
print(f'Dictionary with using "Counter", where the keys are elements of a string and the values are the quantity of those elements: {result_dict}')

print('2 way: With loop')
result_link2 = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'
result_dictionary = {}
for element in result_link2:
    if element in result_dictionary:
        result_dictionary[element] += 1
    else:
        result_dictionary[element] = 1
print(f'Dictionary where the keys are elements of a string and the values are the quantity of those elements: {result_dictionary}')
