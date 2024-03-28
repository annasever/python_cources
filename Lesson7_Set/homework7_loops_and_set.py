# # Task 1
print('Task 1: \'Unique list\'')
first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
unique_first = set(first)
unique_second = set(second)
unique_common_numbers = unique_first.intersection(unique_second)
print(f'List with unique common numbers it is: {list(unique_common_numbers)}.')

# Task 2
print('\nTask 2: \'Missing_elements\'')
first_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
first_set = set(first_list)
second_set = set(second_list)
missing_elements = first_set - second_set
print(f'Elements that are absent in the second list: {missing_elements}.')

# Task 3
print('\nTask 3: \'Unique numbers\'')
print('1 way: Checking of Unique numbers')
numbers = input('Enter numbers for check to unique: ').split()
numbers_in_set = set(numbers)
if len(numbers) == len(numbers_in_set):
    print(f'The list {numbers} contain only unique elements.')
else:
    print('This list contains duplicate elements.')

print('2 way: Checking of Unique numbers with detail explaining')
numbers = input('Enter numbers for check to unique: ').split()
unique_numbers = []
for number in numbers:
    if numbers.count(number) == 1:
        unique_numbers.append(number)
if unique_numbers:
    print(f'The list {numbers} contains the following unique elements: {unique_numbers}.')
else:
    print('This list contains only duplicate elements.')

# Task 4
print('\nTask 4: \'Minimum value\'')
print('1 way')
elements1 = [1, 5, -300, 0, 5, 10, 2, 68, 0]
sorted_set = sorted(set(elements1))
print(f'Mimimum value it is: {sorted_set[0]}.')

print('2 way')
elements2 = [1, 5, -300, 0, 5, 10, 2, 68, 0]
min_element = elements2[0]
for element in elements2:
    if element < min_element:
        min_element = element
print(f'Mimimum value it is: {min_element}.')

# Task 5
print('\nTask 5: \'Sum of all elements\'')
numbers_for_addition = [1, 5, 50, 0, 5, 10, 2, 68]
sum_of_numbers = 0
for i in numbers_for_addition:
    sum_of_numbers += i
print(f'After adding all elements from {numbers_for_addition}, we get {sum_of_numbers}.')
