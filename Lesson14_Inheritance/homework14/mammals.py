from abc import ABC, abstractmethod

from Lesson14_Inheritance.homework14.animals import Animals


class Mammals(Animals):
    def __init__(self, animal, habitat):
        super().__init__(animal)
        self.habitat = habitat

    def live(self):
        return f'{self.animal} lives in {self.habitat}.'

    @abstractmethod
    def reproduce(self):
        pass

    def reproduce(self):
        return f'{self.animal} reproduces by giving birth to cubs.'


if __name__ == '__main__':
    zebra = Mammals('Zebra', 'Africa')
    print(zebra.live())
    print(zebra.reproduce())
