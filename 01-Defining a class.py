class Tree(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print('This is a {} tree and it is {} years old'.format(self.name, self.age))

    def set_age(self, age):
        self.age = age

    def set_weight(self, weight):
        self.weight = weight


t = Tree('Neem', 100)
t.set_age(101)
t.set_weight(500)
print(t.weight)
