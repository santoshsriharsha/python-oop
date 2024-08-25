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

    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

    def __gt__(self, p):
        return len(self) > len(p)

    def __ge__(self, p):
        return len(self) >= len(p)

    def __lt__(self, p):
        return len(self) < len(p)

    def __le__(self, p):
        return len(self) <= len(p)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y


p1 = Point(4,3)
p2 = Point(7, 10)
p3 = Point(2, 6)
p4 = Point(3, 8)
print(len(p1))
print(p1 > p4, p1 <= p3, p1 == p1)