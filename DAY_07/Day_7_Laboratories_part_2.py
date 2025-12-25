from functools import lru_cache

TREE_SOURCE = []
with open("Day_7_Laboratories_input.txt", "r") as f:
    for line in f:
        TREE_SOURCE.append(list(line.rstrip()))

def path_counter(grid, start):
    rows, cols = len(grid), len(grid[0])

    @lru_cache(None)
    def dfs(x, y):
        if not (0 <= y < cols):
            return 0
        if x >= rows:
            return 0
        if x == rows - 1:
            return 1
        cell = grid[x][y]
        if cell == '^':
            return dfs(x + 1, y - 1) + dfs(x + 1, y + 1)
        return dfs(x + 1, y)
    return dfs(*start)


start = (0, 70)
COUNT = path_counter(TREE_SOURCE, start)
print(f'\n>>> PATHS NUMBER {COUNT}')

