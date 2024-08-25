class Tree(object):
    def __init__(self, name):
        self.name = name

    def details(self):
        print('This is a {} tree'.format(self.name))


t = Tree('Neem')
t.details()