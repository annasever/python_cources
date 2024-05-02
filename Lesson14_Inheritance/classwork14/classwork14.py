# 1-------------------------------------------
# Inheritance
# IS-A
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def breath(self):
#         return f'{self.name} can breath'
#
# class Employee(Human):
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#
#     def calculate_salary(self):
#         return self.salary + self.__calculate_bonus()
#
#     def __calculate_bonus(self) -> float:
#         return self.salary * self.bonus // 100
#
# class Developer(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary, 10)
#
# class AQA(Employee):
#
#     def __init__(self, name, salary, bonus=5):
#         super().__init__(name, salary, bonus)
#
#
# class Manager(Employee):
#     def __init__(self, name, salary, bonus=50):
#         super().__init__(name, salary, bonus)
#
#     def create_report(self):
#         return 'I can create report'
#
# if __name__ == '__main__':
#     maryna = AQA('Maryna', 5000)
#     oleg = Developer('Oleg', 7000)
#     nastya = Manager('Nastya', 10_000)
#     print(maryna.calculate_salary())
#     print(oleg.calculate_salary())
#     print(nastya.calculate_salary())
#     print(Manager.mro())
#     print(nastya.breath())

# 2----------------------------------
# MultiInheritance
# class Father:
#     def __init__(self):
#         self.strength = 40
#     def do_workout(self):
#         return f'Do workout with strendth {self.strength}'
# class Mother:
#     def __init__(self):
#         self.wisdom = 60
#     def read_books(self):
#         return f'Read books with wisdom {self.wisdom}'
# class Child(Father, Mother):
#
#     def __init__(self):
#         Father.__init__(self)
#         Mother.__init__(self)
#
#     def play(self):
#         return  'I play'
#
# if __name__ == '__main__':
#     tom = Child()
#     print(tom.do_workout())
#     print(tom.read_books())
#     print(tom.play())
#     print(Child.mro)

# 3-------------------------------------------------
# Multiinheritance with error
# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# class D (C, B):
#     pass
# error:
# class E(B, C ,D):
#     pass

# class E(D):
#     pass
# if __name__ == '__main__':
#     test = E()

# 4---------------------------------------------
# Abstraction
# from abc import ABC, abstractmethod
# class Employee(ABC):
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#     @abstractmethod
#     def do_work(self):
#         pass
#
#     def calculate_salary(self):
#         return self.salary + self.calculate_bonus()
#
#     def calculate_bonus(self) -> float:
#         return self.salary * self.bonus // 100
#
# class Cleaner(Employee):
#
#     def __init__(self, name, salary):
#         super().__init__(name, salary, 3)
#
#     def do_work(self):
#         return 'I like my job'
#
#     # def calculate_salary(self):
#     #     return self.salary
#     #
#     # def calculate_bonus(self):
#     #     return self.bonus
#
# if __name__ == '__main__':
#     tanya = Cleaner('Tanya', 600)
#     print(tanya.calculate_salary())
#     print(tanya.calculate_bonus())
#     print(tanya.do_work())

# 5------------------------------------------------
# Polymorfism
# class Animal:
#     def make_noise(self):
#         return 'Make noize'
# class Cat(Animal):
#     def make_noise(self):
#         return 'Meow'
#
# class Dog(Animal):
#     def make_noise(self):
#         return 'Woof'
#
# def noise(animal: Animal):
#     return animal.make_noise()
#
# if __name__ == '__main__':
#     print(noise(Cat()))
#     print(noise(Dog()))

# 6---------------------------------------------------
# Generator
# def square():
#     print('Generator work')
#     for i in range(1, 11, 2):
#         yield i ** 2
# gen = square()
# # print(next(gen))
# # print(next(gen))
#
# for i in gen:
#     print(i)
# print(dir(gen))

def pause():

    while True:
        print(a)
        yield a
if __name__ == '__main__':
    gen = pause()
    print(gen)
    a = 10
    next(gen)
    a = 20
    next(gen)
    next(gen)


