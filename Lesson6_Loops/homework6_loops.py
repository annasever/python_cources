# Task 1
print('Task 1: \'Division program\'')
numbers = input('Enter numbers separated by spaces: ').split()
denominator = int(input('Enter denominator: '))
divisible_numbers = []
for number in numbers:
    if int(number) % denominator == 0:
        divisible_numbers.append(number)
if len(divisible_numbers) == 0:
    print(f'Numbers divisible by {denominator} is absend')
else:
    print(f'Numbers divisible by {denominator} are: {divisible_numbers}')

# Task 2
print('\nTask 2: \'List consistency check\'')
numbers_for_check = [1, 2, 3, 5, 6, 7, 8, 9]
for i in range(1, len(numbers_for_check)):
    if numbers_for_check[i] != numbers_for_check[i-1] + 1:
        print(f'The first is not sequential number:{numbers_for_check[i]} ')
        break
else:
    print('The list is sequential')


# Task 3
print('\nTask 2: \'Create figure\'')
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()
