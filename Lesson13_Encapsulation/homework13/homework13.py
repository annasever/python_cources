class DevOps:
    def __init__(self, name, experience, salary):
        self._name = name
        self._experience = experience
        self._salary = salary

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, word):
        if not isinstance(word, str):
            raise ValueError('Name must be a string')
        self._name = word

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, years):
        if not isinstance(years, int):
            raise ValueError('Experience must be a number')
        self._experience = years

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Salary must be a number")
        if value < 0:
            raise ValueError("Salary can/`t be negative")
        self._salary = value

    def __str__(self):
        return (f'{self.__class__.__name__} named {self._name} '
                f'who has {self._experience} years of experience and a salary of {self._salary}$.')


if __name__ == '__main__':
    anna = DevOps('Anna', 5, 5000)
    print(anna)
