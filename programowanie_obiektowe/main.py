from random import uniform
from Classes import Point, Circle

points = [Point(uniform(-5,5), uniform(-5,5)) for _ in range(100)]

circles =[
Circle(0,0,4),
Circle(2,3,2),
Circle(-1,2,3)
]

points_in_circle, points_beyond_circles = [], []

for i, point in enumerate(points):
    counter = 0
    for circle in circles:
        if point.distance_to(circle) <= circle.radius:
            counter += 1
    if counter == 3:
        points_in_circle.append(point)
    elif counter == 0:
        points_beyond_circles.append(point)

print(f"liczba punktów w kołach: {len(points_in_circle)}")
for point in points_in_circle:
    print(point, end="")
print()

print(f"liczba punktów poza kołami: {len(points_beyond_circles)}")
for point in points_beyond_circles:
    print(point, end="")