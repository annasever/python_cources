# fruits = {'orange': 50, 'apple': 20, 'banana': 40}
# print(fruits['orange'])
# print(fruits.get('banana'))
# print(fruits.get('age'))
# print(fruits.get('age', False))
# print(fruits.get('name', 'Key is not found'))

# from timeit import  timeit
# my_dict = {}
# my_dict1 = dict()
# print(timeit('{}'))
# print(timeit('dict()'))

# my_dict = {'name': 'Maryna', 'age': 31, 'job': 'AQA'}
# my_dict1 = dict(name='Maryna', age=31, job='AQA')
# print(my_dict)
# print(my_dict1)
# my_dict2 = dict.fromkeys(['test', 1, 2, 3, 4], ['first', 'second'])
# print(my_dict2)

# my_dict = {'name': 'Maryna', 'age': 31, 'job': 'AQA'}
# my_dict['age_1'] = my_dict.get('age_1', 0) +1
# my_dict['salary'] = 1_000_000
# my_dict['job'] = 'admin'
# print(my_dict.items())
# new_dict = {'name2': 'Rita', 'language': 'Python'}
# my_dict.update(new_dict)
# print(my_dict)

# my_dict = {'name': 'Maryna', 'age': 31, 'job': 'AQA'}
# new_dict = {'name2': 'Rita', 'language': 'Python'}
# # my_dict.setdefault('language')
# # my_dict.pop('name')
# print(sorted(my_dict))
# print(my_dict)

# test = {1: 'test', 2: 'second'}
# for element in test.items():
#     print(element, end=', ')
# for key, value in test.items():
#     print(value, end=', ')


# family = {
#     'grandpa': ('Alex', 76),
#     'grandma': ('Nona', 74),
#     'dad': ('Greg', 48),
#     'mom': ('July', 45),
#     'son': ('Mark', 10)
# }
# ages =[]
# for name, age in family.values():
#     ages.append(age)
#
# result = max(ages) - min(ages)
# print(f'Difference between elder and younger person is {result}')
