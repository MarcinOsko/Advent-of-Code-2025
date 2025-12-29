import itertools

points = []
pairs = []
resoult = 0

with open("Day_9_Movie_Theater_input.txt", "r") as f:
    for line in f:
        points.append(tuple(map(int, line.split(","))))

rectangle_field = 0

def rect_field(p1, p2):
    edge1 = abs(p2[0] - p1[0]) + 1
    edge2 = abs(p2[1] - p1[1]) + 1
    return  edge1 * edge2

pairs  = list(itertools.combinations(points, 2))

for rect in itertools.combinations(points, 2):
    if rect_field(rect[0], rect[1]) > resoult:
        resoult = rect_field(rect[0], rect[1])

print(f'\n>>> The area of the largest possible rectangle is: {resoult}')
