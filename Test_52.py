class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return((other.x - self.x)**2 + (other.y - self.y)**2)**(1/2)


p1 = Point(1, 1)
p2 = Point(3, 3)
print(Point.distance(p1, p2))
