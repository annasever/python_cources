# names = ['Maryna', 'Olga', 'Ivan']
# ages = [31, 45, 15]
# print(names[0])
# print(names[len(names)-1])
# print(id(names))
# names.append('Ira')
# print(names)
# print(id(names))
first = ['one', 'two']
# second = ['three', 'four']
# first.extend(second)
# print(first)
# third = ['2', '2']
# first.append(third)
# print(first)
# fought = 'abc'
# first.extend(fought)
# print(first)
# first.append(fought)
# print(first)
# age =[0, 98, -109, -1, 76, 3]
# age.sort()
# print(age)

names = ['Maryna', 'Olga', 'Ivan', 'lila', 'lola', '15']
new_list = names.copy()
new_list.append('test')
print(names)
print(new_list)
new = sorted(names)
print(new)


# my_str = 'Hillel IT school'
# print(my_str.split())
#
# names = ['Hillel', 'IT', 'school']
# print(' '.join(names))

# Hw5
data_list = ['London', 'Paris', '33', 'Berlin', '100', '0']
data_list_lower = data_list.sort(key=str.lower)
data_list_upper = data_list.sort(key=str.upper)
if data_list == data_list.sort(key=str.lower):
    check_on_lower = True
    print(f'The statement that this string is sorted is {check_on_lower}')
elif data_list == data_list.sort(key=str.upper):
    check_on_upper = True
    print(f'The statement that this string is sorted is {check_on_upper}')
else:
    print('This list is not sorted')
