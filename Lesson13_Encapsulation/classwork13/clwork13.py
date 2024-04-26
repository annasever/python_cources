from Lesson13_Encapsulation.classwork13.classwork13 import Human

if __name__ == '__main__':
    olga = Human('Olga', 29)
    print(olga)
    olga._name = 'Oleg'
    olga.__age = 43
    print(olga)
    olga._Human__age = 43
    print(olga)
    olga.name = 'Nata'
    print(olga)
    olga.age = 50
    print(olga)
    del olga._name