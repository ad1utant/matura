import math

class Point:
    def __init__(self, x, y):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)) :
            self.x, self.y = x, y
        else:
            raise TypeError

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            if (self.x, self.y) == (other.x, other.y):
                return True
        return False

    def distance_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError

    def __eq__(self, other):
        if isinstance(other, Circle):
            if super().__eq__(other) and self.radius == other.radius:
                return True
        return False

    def __repr__(self):
        return f"Circle({self.x}, {self.y}, {self.radius})"

    def __str__(self):
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"

    def edge_distance_from_origin(self):
        return super().distance_from_origin() - self.radius

    def area(self):
        return self.radius**2*3.14

    def circumference(self):
        return 2 * 3.14 * self.radius