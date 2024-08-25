class Dog(object):

    dogs = []

    def __init__(self, name):
        self.name = name
        Dog.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        for _ in range(n):
            print('Bark!')


d = Dog('Tommy')
Dog.num_dogs()
Dog.bark(5)
