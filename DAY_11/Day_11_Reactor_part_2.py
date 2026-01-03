from functools import lru_cache
from pprint import pprint

with open("Day_11_Reactor_input.txt", "r") as f:
    data = f.read()

graph = {}
for line in data.strip().split("\n"):
    key, values = line.split(":")
    graph[key.strip()] = values.strip().split()

print("-" * 50)
print("INPUT GRAPH:")
pprint(graph)
print("-" * 50)


@lru_cache(None)
def count_paths(node, seen_fft, seen_dac):
    if node == "out":
        return 1 if seen_fft and seen_dac else 0
    if node not in graph:
        return 0
    total = 0
    for nxt in graph[node]:
        total += count_paths(
            nxt,
            seen_fft or (nxt == "fft"),
            seen_dac or (nxt == "dac")
        )
    return total

result = count_paths("svr", False, False)

print("LICZBA POPRAWNYCH ŚCIEŻEK:", result)
print("-" * 50)
