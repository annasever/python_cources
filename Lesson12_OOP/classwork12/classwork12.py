# 1----------------------------------------
# a, *b = 1, 2, 3
#
# if __name__ == '__main__':
#     print(a)
#     print(b)
#     print(c)

# 2---------------------------------------
# a, *b, c = 1, 2, 3, 4, 5, 6
#
# if __name__ == '__main__':
#     print(a)
#     print(b)
#     print(c)

# 3---------------------------------------
# def custom_sum(*args):
#     result = 0
#     for arg in args:
#         result += arg
#     return result
#
# if __name__ == '__main__':
#     print(custom_sum(1, 2, 10))

# 4---------------------------------------
# def example(a, b, /, c):
#     print(a)
#     print(b)
#     print(c)
# if __name__ == '__main__':
#     example(1, 2, c=3)\

# 5-----------------------------
# def example(a, b, *, c, d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#
# if __name__ == '__main__':
#     example(1, 2, c=3, d=4)

# 6-----------------------------------
# def custom_sum(*args, **kwargs):
#     result = 0
#     for arg in args:
#         result += arg
#     print(kwargs)
#     return result
#
# if __name__ == '__main__':
#     print(custom_sum(1, 2, 10, a=10, b=11))

# 7__________________________________
# my_dict = { 'sep': '+', 'end': '$'}
# print('Hello world', 'Test', **my_dict)

# 8-------------------------------------
# class Car:
#     pass
#
#     def move(self):
#         print(self)
#         return 'I go'
#
# if __name__ == '__main__':
#     bmw = Car()
#     audi = Car()
#     print(type(bmw))
#     print(bmw.move())
#     print(audi.move())
    
# 9-------------------------------------
# class Car:
#
#     def move(self, name):
#         print(self)
#         return f'I go {name}'
#
# if __name__ == '__main__':
#     bmw = Car()
#     audi = Car()
#     print(type(bmw))
#     print(bmw.move('BMW'))
#     print(audi.move('Audi'))

# 10-------------------------------------
class Car:

    def __init__(self, mark, age, model):
        self.mark = mark
        self.age = age
        self.model = model

    def move(self):
        print(self)
        return f'{self.model} is going'

    def turn_left(self):
        pass

if __name__ == '__main__':
    bmw = Car('BMW', 2023, 'X5')
    audi = Car('Audi', 2022, 'Q8' )
    print(bmw.mark)
    print(bmw.move())
