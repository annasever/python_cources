# Task 1
print('Task 1: \"Removing letters\"')
fruits = 'apple mango banana'
my_str = input('Enter string: ')
letters = input('Enter letter to delete: ')
result1 = my_str.replace((letters), '')
print(f'Enter string without specified letters: {result1}')

# Task 2
print('\nTask 2: \"Capital letters\"')
text = 'This is some test STRING'
my_text = input('Enter string: ')
result2 = my_text.title()
print(f'Enter string with capital letters: {result2}')

# Task 3
print('\nTask 3: \"Reverse strings\"')
browser = 'Google Chrome'
my_browser = input('Enter browser name: ')
result3 = my_browser[::-1]
print(f'Enter with reverse string : {result3}')

# Task 4
print('\nTask 4: \"Compare of strings\"')
string_1 = 'abcdef12345'
string_2 = 'London Paris'
string__1 = input('Enter first string: ')
string__2 = input('Enter second string: ')

if len(string__1) == len(string__2) != 0:
    print('The strings match')
elif len(string__1) > len(string__2):
    print('The first string is longer than the second')
elif len(string__1) < len(string__2):
    print('The first string is shorter than the second')
else:
    print('Both strings are empty')


# Task 5
print('\nTask 5: \"Repeat of string\"')
date = '13.03.2024'
current_date = input('Enter the current date: ')
repeat = int(input('Enter number of repeats: '))
result4 = current_date * repeat
print(f'Repetition program: {result4}')

# Task 6
print('\nTask 6: \"$$$Currency Exchange$$$\"')
usd_uah = 38.3
eur_uah = 41.8

currency1 = input('Enter currency to sell (uah, usd, eur): ')
currency2 = input('Enter currency to buy (uah, usd, eur): ')
amount_of_money = input(f'How much {currency1} you want to exchange?: ')

if currency1 == 'uah' and currency2 == 'usd':
    result5 = round(float(amount_of_money) / usd_uah, 2)
    print(f'After exchange {amount_of_money} {currency1} you give {result5} {currency2}')
elif currency1 == 'usd' and currency2 == 'uah':
    result6 = round(float(amount_of_money) * usd_uah, 2)
    print(f'After exchange {amount_of_money} {currency1} you give {result6} {currency2}')
elif currency1 == 'uah' and currency2 == 'eur':
    result7 = round(float(amount_of_money) / eur_uah, 2)
    print(f'After exchange {amount_of_money} {currency1} you give {result7} {currency2}')
elif currency1 == 'eur' and currency2 == 'uah':
    result8 = round(float(amount_of_money) * eur_uah, 2)
    print(f'After exchange {amount_of_money} {currency1} you give {result8} {currency2}')
else:
    print(f'Sorry but exchanging from {currency1} to {currency2} is not supported')
