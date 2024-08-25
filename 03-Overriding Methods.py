class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y


p1 = Point(4,3)
p2 = Point(7, 10)
p3 = Point(2, 6)
p4 = Point(3, 8)