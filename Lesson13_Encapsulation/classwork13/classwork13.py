# 1---------------------------
# def square(number: int):
#     return number ** 2
#
# square_2 = lambda number: number ** 2
#
# if __name__ == '__main__':
#      print(square(2))
#      print(square_2(3))

# 2_________________________________
# def test():
#     return 'Hello'
# test2 = lambda: 'Hello'
# if __name__ == '__main__':
#     print(test())
#     print(test2)

# 3-------------------------
# def even_odd(number):
#     return 'EVEN' if number % 2 == 0 else 'ODD'
#
# even_odd2 = lambda number: 'EVEN' if number % 2 == 0 else 'ODD'
#
# if __name__ == '__main__':
#     print(even_odd(6))
#     print(even_odd2(9))

# 4__________________________________________
# square_2 = lambda number: number ** 2
# print(square_2(3))

# 5------------------------------------
# if __name__ == '__main__':
#     x = 2
#     result = lambda n=x : n ** 2
#     x = 3
#     result_2 = lambda n=x : n ** 3
#     print(result())
#     print(result_2())

# 6------------------------------------------
# if __name__ == '__main__':
#     number = list(range(10))
#     def even_numbers(num):
#         return num % 2 ==0
#     result = list(filter(even_numbers, number))
#
#     result_filter = list(filter(lambda num: num % 2 == 0, number))
#
#     result_map = list(map(lambda number: number ** 2, result))
#
#     print(result)
#     print(result_filter)
#     print(result_map)

# 7----------------------------------------
# my_dict = {'d': 1, 'a': 4, 'b': 2}
# sorted_dict = sorted(my_dict.items(), key=lambda x: x[1])
# print(sorted_dict)

# 8-----------------------------------------------------------
# class Toshiba:
#     def __init__(self, age):
#         self.age = age
#
#     def __str__(self):
#         return f'STR Company {self.__class__.__name__} with age {self.age}'
#
#     def __repr__(self):
#         return f'REPR Company {self.__class__.__name__} with age {self.age}'
# if __name__ == '__main__':
#     lol = Toshiba(1990)
#     print(lol)

# 9-------------------------------------------------------------

# class Human:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#     def __str__(self):
#         return f'{self.__class__.__name__} with name {self._name} and {self.__age}'
#
#     def get_name(self):
#         return self._name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self):
#         if 0 > new_age > 100:
#             raise ValueError('Invalid age')
#         self.__age = new_age

    # @property
    # def name(self):
    #     return self._name
    #
    # @name.setter
    # def name(self, new_name):
    #     if not new_name.isalpha():
    #         raise ValueError('Name should contain only letters')
    #     self._name = new_name
    #
    # @name.deleter
    # def name(self):
    #     raise PermissionError('You can\`t delete attribute')
    #
    #
    # @property
    # def age(self):
    #     raise PermissionError('You dont have permission')
    #
    # @age.setter
    # def age(self, new_name):
    #     if 0 > new_age > 100:
    #         raise ValueError('Invalid age')
    #     self.__age = new_age
#
#
# if __name__ == '__main__':
#     tom = Human('Tom', 20)
#     print(tom)
#     tom.name = 'John'
#     print(tom)

# 10 ---------------------------------------------
class Human:
    def __init__(self, name, age, gender=None):
        self._name = name
        self.__age = age
        self.__gender = gender

    def __str__(self):
        return f'{self.__class__.__name__} with name {self._name} and {self.__age}'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name.isalpha():
            raise ValueError('Name should contain only letters')
        self._name = new_name
if __name__ == '__main__':
    anna = Human('Anna', 28)
    print(anna)
#
#     @name.deleter
#     def name(self):
#         raise PermissionError('You can\`t delete attribute')
#
#     @property
#     def age(self):
#         raise PermissionError('You dont have permission')
#
#     @age.setter
#     def age(self, new_age):
#         if 0 > new_age > 100:
#             raise ValueError('Invalid age')
#         self.__age = new_age
#
#     def __calculate_salary_according_gender(self):
#         return ''

# 11---------------------------------------------

# class Developer:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#         self.bonus = 15
#
#     def __calculate_bonus(self) -> int:
#         return self.salary * self.bonus // 100
#     def calculate_salary(self) -> int:
#         return self.salary + self.__calculate_bonus()
#
# if __name__ == '__main__':
#     tom = Developer('Tom', 'Senior', 4500)
#     lera = Developer('Lera', 'Middle', 300)
#     print(tom.calculate_salary())
#     print(lera.calculate_salary())
