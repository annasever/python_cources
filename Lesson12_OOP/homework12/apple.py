class Apple:
    def __init__(self, device, model, year, color):
        self.device = device
        self.model = model
        self.year = year
        self.color = color

    def show(self):
        return f'There are {self.color} {self.device} {self.model} from {self.__class__.__name__} at {self.year}'


if __name__ == '__main__':
    iphone = Apple('IPhone', '14', '2023', 'white')
    print(iphone.show())
