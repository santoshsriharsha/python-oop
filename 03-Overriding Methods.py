class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)


p1 = Point(4,3)
p2 = Point(7, 10)
p3 = Point(2, 6)
p4 = Point(3, 8)
p5 = p1 + p2
p6 = p3 - p4
p7 = p1 * p4

print(p5, p6, p7)