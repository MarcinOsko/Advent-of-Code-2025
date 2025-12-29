import math
from itertools import combinations

points = []
EDGES = []

with open("Day_8_Playground_input.txt", "r") as f:
    for line in f:
        points.append(tuple(map(int, line.split(","))))

edges = []
for i, j in combinations(range(len(points)), 2):
    edges.append((math.dist(points[i], points[j]), i, j))

edges.sort()

parent = list(range(len(points)))
size = [1] * len(points)
components = len(points)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    global components
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    components -= 1
    return True


last_edge = None

for _, a, b in edges:
    if union(a, b):
        last_edge = (a, b)
        if components == 1:
            break

x1 = points[last_edge[0]][0]
x2 = points[last_edge[1]][0]
print(x1 * x2)
