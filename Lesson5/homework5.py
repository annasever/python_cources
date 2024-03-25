# 1 Task
print('Task 1: \"Palindrome\"')
my_str = input("Enter string for check: ")
if (my_str == my_str[::-1]):
    first_check = True
    print(f'The statement that this string is palindrome is {first_check}')
else:
    second_check = False
    print(f'The statement that this string is palindrome is {second_check}')

# 2 Task
print('\nTask 2: \"List_string_list\"')
my_list =  ['Hillel', 'AQA', 'TEST']
print(' '.join(my_list))
print((' '.join(my_list)).split())

# 3 Task
print('\nTask 3: \"Sorted list\"')
sorted_list = ['Tst', 'aBc', 'TEST', 'Hello', 'neW']
sorted_list.sort(key=str.lower)
print(sorted_list)

# 4 Task
print('\nTask 4: \"To got: [\'Win\']\"')
list_1 = [1, 2, 3, 4, 5, 6, [1, 2, 3, ['Win']]]
print(list_1 [-1][-1])

# 5 Task
print('\nTask 5: \"Sorting correctness\"')
data = ['London', 'Paris', '33', 'Berlin', '100']
data_list = input('Enter list for check sorting correctness: ')
sort_data_list = sorted(data_list)

if data_list == sort_data_list:
    print('This list is sorted correctly')
else:
    print('This list is not sorted correctly')
<<<<<<< HEAD
=======
    
>>>>>>> ee1bfad74e0a13b527c9ae202a286be067b6565c
