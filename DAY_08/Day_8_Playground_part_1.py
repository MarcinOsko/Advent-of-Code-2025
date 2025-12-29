import math
from itertools import combinations

points = []
edges = []

with open("Day_8_Playground_input.txt", "r") as f:
    for line in f:
        points.append(tuple(map(int, line.split(","))))

for A, B in combinations(points, 2):
    edges.append((math.dist(A, B), A, B))

edges.sort()

circuits = [{p} for p in points]


def circ_finder(p):
    for c in circuits:
        if p in c:
            return c


for _, A, B in edges[:1000]:
    c1 = circ_finder(A)
    c2 = circ_finder(B)

    if c1 is not c2:
        c1.update(c2)
        circuits.remove(c2)

sizes = sorted((len(c) for c in circuits), reverse=True)
print(sizes)
print(sizes[0] * sizes[1] * sizes[2])
