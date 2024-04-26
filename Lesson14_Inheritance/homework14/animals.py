class Animals:
    def __init__(self, animal):
        self.animal = animal

    def _existence(self):
        return f'{self.animal} it is wonderful animal.'


if __name__ == '__main__':
    lion = Animals('Lion')
    print(lion._existence())
