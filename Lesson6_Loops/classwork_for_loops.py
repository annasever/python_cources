# for i in range(5):
#     print('Meow')
#
# num = 4
# for _ in range(num + 1):
#     print(_)

# numbers = [1, 2, 3, 4, 5, 6,7, 8]
# for i in numbers:
#     print(i, end=' ')

# num = ['one', 'two', 'three', 'two']
# # for number in num:
# #     print(number, end=' ')
# for number in num:
#     lol = num.index(number)
#     if number in num[lol + 1:]:
#         num.remove(number)
# print(num)

# numbers = [1, 29, 66, 87, 100, 53, 24, 23]
# even_numbers = list()
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)

# numbers = [1, 29, 66, 87, 100, 53, 24, 23]
# even_numbers = list()
# for number in numbers:
#     if number == 100:
#         continue
# print(f'My number {number}')

# numbers = [1, 29, 66, 87, 100, 53, 24, 23]
# even_numbers = list()
# for number in numbers:
#      if number == 53:
#          break
# print(f'My number {number}')
#
# numbers = [1, 29, 66, 87, 100, 53, 24, 23, 29, 1]
# unique= []
# for number in numbers:
#     if numbers.count(number) == 1:
#        unique.append(number)
#
# print(unique)

# for i in range(5):
#     print('*' * (i + 1))

# for i in range(1, 6):
#     print('* ' * i )

# variable =6
# for i in range(1, 6):
#     print(variable * ' ', '* ' * i)
#     variable -= 1

# numbers = [1, 2, 3]
# letters = 'abc'
# names = ['Anna', 'Olga']
# for number in numbers:
#     for letter in letters:
#         for name in names:
#             print(number, letter, name)

# width = 5
# height = 5
#
# for i in range(1, height):
#     for j in range(1, width):
#         print('*', end=' ')
#     print()

# names = ['Anna', 'Olga', 'Oleg']
# filtered = []
# for name in names:
#     if name == 'Oleg':
#         continue
#     filtered.append(name)
# print(filtered)
#
# names = ['Anna', 'Olga', 'Oleg']
# filtered = [name for name in names if name != 'Oleg']
# print(filtered)

# data = input('Enter your string: ').lower()
# vowels = 'aieouy'
# count = 0
#
# for letter in data:
#     if letter in vowels:
#         count += 1
# print(f'Count of vowels letters in {data} string is {count}')

# data = input('Enter your string: ')
# vowels = 'aieouy'
# count = 0
#
# for letter in data.lower():
#     if letter in vowels:
#         count += 1
# print(f'Count of vowels letters in {data} string is {count}')

# data = input('Enter your string: ').lower()
# vowels = 'aieouy'
# my_list = []
#
# for letter in data:
#     if letter in vowels:
#         my_list.append(letter)
# print(f'Count of vowels letters in {data} string is {my_list}')

# data = input('Enter your string: ').lower()
# vowels = 'aieouy'
# my_list = [letter for letter in data if letter in vowels]
# print(my_list)


