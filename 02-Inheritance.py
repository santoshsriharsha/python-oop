class Tree(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print('This is a {} tree and it is {} years old'.format(self.name, self.age))


class Plant(Tree):
    def __init__(self, name, age, location):
        super().__init__(name, age)
        self.location = location


t = Tree('Neem', 100)
p = Plant('Tulasi', 5, 'Farm House')
t.details()
p.details()
