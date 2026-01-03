from pprint import pprint

data = ''

with open("Day_11_Reactor_input.txt", "r") as f:
    for l in f:
        data += l

graph = {}
for line in data.strip().split("\n"):
    key, values = line.split(":")
    graph[key.strip()] = values.strip().split()

print(50*'-')
print("INPUT GRAPH:")
pprint(graph)
print(50*'-')

def find_paths(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]

    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        new_paths = find_paths(graph, node, end, path)
        for p in new_paths:
            paths.append(p)
    return paths

all_paths = find_paths(graph, 'you', 'out')

print("ALL PATHS:")
for p in all_paths:
    print(" -> ".join(p))
print(50*'-')
print("PATHS NUMBER:", len(all_paths))
print(50*'-')
