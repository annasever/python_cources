from Lesson14_Inheritance.homework14.mammals import Mammals


class Predators(Mammals):
    def __init__(self, animal, habitat, food):
        super().__init__(animal, habitat)
        self.food = food

    def live_and_eat(self):
        return f'{self.animal} lives in {self.habitat} and eats {self.food}.'


if __name__ == '__main__':
    tiger = Predators('Tiger', 'Savannah', 'zebra')
    print(tiger.live_and_eat())
