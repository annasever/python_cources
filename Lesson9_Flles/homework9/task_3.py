# Receive value after writing key.
course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
input_key = input('Enter key: ')
result = []

for key, value in course.items():
    if input_key == key:
        result = value
        break
if result:
    print(f'Key {input_key} has value {result}.')
# else:
#     print(f'Key {input_key} not found in the dictionary.')

try:
    result = course[input_key]
#   print(f'Key {input_key} has value {result}.')
except KeyError:
    print(f'Key {input_key} leads to KeyError')
