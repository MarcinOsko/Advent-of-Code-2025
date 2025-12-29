import pprint
from pprint import pprint


POINTS = []

with open("test.txt", "r") as f:
    for line in f:
        POINTS.append(tuple(map(int, line.split(","))))

pprint(POINTS)

