# my_set = set()
# my_set1 = {1, 2, 3, 5}
# my_set2 = {1, 1, 2, 3, 5, 'test', False, 0, (1, 2), 'test'}
# # print(type(my_set))
# # print(type(my_set1))
# # print(type(my_set2))
# my_set2.add('abs')
# print(my_set2)

# my_list = [1, 2, 3 ,3, 4, 5, 5, 6]
# print(list(set(my_list)))

# myset = {1, 2, 3, 3, 4, 5, 5, 6}
# myset.add('new')
# myset.update([1, 2, 3, 4, 5])
# myset.update('test')
# myset.update(['test_test'])
# for letter in ['test_test']:
#     myset.add(letter)
# print(myset)
# myset.remove(1)
# myset.discard('abc')
# print(myset)

# set1 = {1, 2, 3, 10, 4, 5}
# set2 = {4, 5, 6, 7, 8, 9, 0}
# set3 = sorted(set2)
# print(set3)
# set4 = sorted(set(set2))
# print(set4)

# set3 = set1 | set2
# print(set3)
# set4 = set2.difference(set1)
# print(set4)
# set5 = set1.symmetric_difference(set2)
# print(set5)
# set6 = set1.intersection(set2)
# print(set6)

# set1 = {1, 2, 3, 10, 4, 5}
# set2 = {4, 5, 6, 7, 8, 9, 0}
#
# for element in set1:
#     print(f'Element {element}')


# set1 = {1, 2, 3, 10, 4, 5}
# set2 = {4, 5, 6, 7, 8, 9, 0}
# set3 = set()
#
# for element in range(1,10,2):
#     if element ==7:
#         continue
#     set3.add(element)
# print(set3)
#
# set3 = {element for element in range(1, 10, 2) if element != 3}
# print(set3)

# import random
# # set1 = {1, 2, 3, 10, 4, 5}
# # set2 = {4, 5, 6, 7, 8, 9, 0}
# set3 = set()
# for element in range(1, 10):
#     set3.add(random.randint(1, 10))
#
# # while len(set3) < 10:
# #     number = random.randint(1, 100)
# #     set3.add(number)
#
# print(len(set3))
# print(set3)
