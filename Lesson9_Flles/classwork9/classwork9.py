# file = open('file1.txt', 'r')
# print(file)
# print(file.read(7))
# print(file.tell())
# print(file.seek(0))
# print(file.closed)
# for line in file:
# print(line)
# file = open('file1.txt', 'r')
# print(file.readlines())
# file.close()
# print(file.closed)

# import os
# print(os.getcwd())

# test = open('file1.txt', 'r+')
# print(test.write('Lo'))

# test = open('file1.txt', 'a')
# print(test.write(' Lola'))
# test.close()

# with open('file1.txt', 'r', encoding='utf-8') as file:
#
#     with open('file2.txt', 'w', encoding='utf-8') as new_file:
#         # for line in file:
#         #     new_file.write(line)
#             #Or
#         new_file.writelines(file)

# import csv

# test = []
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#
#     for line in csv_reader:
#         test.append(line[2])
#         # print(line[2])
# print(test)
import csv
# test = []
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('names1.csv', 'w', newline='') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         csv_writer.writerows(csv_reader)
#
# with open('names1.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line[1])
#
# with open('names1.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file, delimiter='\t')
#     for line in csv_reader:
#         print(line['email'])
#-------------------
# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('names1.csv', 'w', newline='') as new_file:
#         fieldnames = ['last_name', 'email']
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='$')
#
#         csv_writer.writeheader()
#
#         for elements in csv_reader:
#             del elements['first_name']
#             csv_writer.writerow(elements)

#---------------------------
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
#
# try:
#     result = first // second
# # except (ZeroDivisionError, TypeError):
# #     result = 'Second number shouldn`t be zero'
# except ZeroDivisionError:
#      result = 'Second number shouldn`t be zero'
# except TypeError:
#     result = 'Type error'
# print(result)
#----------------------------------------------
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# try:
#     if isinstance(first, int) and isinstance(second, int):
#         result = first // second
# except ZeroDivisionError as e:
#      result = e
#      print(result)
# else:
#     print(result)
# #----------------------------------------
# first = int(input('Enter first number: '))
# second = int(input('Enter second number: '))
# try:
#      result = first // second
# except ZeroDivisionError as e:
#      result = e
#      print(result)
# finally:
#     print('End')

# first = input('Enter first number: ')
# if isinstance(first, str):
#     raise TypeError(f'{first} should be integer')

# first = int(input('Enter first number: '))
# assert isinstance(first, int), f'Invalid datatype{type(first)}'
# assert 5 != 5,f'Invalid type'

#-------------
course = {'title': 'AQA', 'language': 'Python', 'level': 'PRO', 'frame': 'pytest'}
input_key = input('Enter key: ')

try:
    result = None
    for key, value in course.items():
        if input_key == key:
            result = value
            break
    if result is not None:
        print(f'Key {input_key} has value {result}.')
    else:
        print(f'Key {input_key} not found in the dictionary.')
except KeyError:
    print(f'Key {input_key} leads to KeyError.')

