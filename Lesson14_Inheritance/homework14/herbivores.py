from Lesson14_Inheritance.homework14.mammals import Mammals


class Herbivores(Mammals):
    def __init__(self, animal, habitat, food, age):
        super().__init__(animal, habitat)
        self._food = food
        self._age = age

    @property
    def food(self):
        return self._food

    @food.setter
    def food(self, word):
        if not isinstance(word, str):
            raise ValueError('Food must be a string')
        self._food = word

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, years):
        if not isinstance(years, int):
            raise ValueError("Years must be a number")
        if years < 0:
            raise ValueError("Years can/`t be negative")
        self._age = years

    def __str__(self):
        return f'{self.animal} that lives for {self._age} years in {self.habitat} and eats {self._food}.'


if __name__ == '__main__':
    antelope = Herbivores('Antelope', 'Savannah', 'grass', 10)
    print(antelope)
