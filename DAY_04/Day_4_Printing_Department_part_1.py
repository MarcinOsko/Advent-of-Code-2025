
GRID = []
SUM = 0
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0,-1), (0,1),
              (1,-1), (1,0), (1,1)]


# with open("Day_4_Printing_Department_input.txt", "r") as f:
#     for line in f:
#         GRID.append(line.strip())

with open("Day_4_Printing_Department_input.txt", "r") as f:
    for line in f:
        GRID.append(line.strip())

grid_lines = len(GRID)
grid_fields = len(GRID[0])
if grid_lines == grid_fields:
    N = grid_lines

neighbors = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        licznik = 0
        if GRID[i][j] == '@':
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    if GRID[ni][nj] == '@':
                        licznik += 1
            if licznik < 4:
                neighbors[i][j] = 'x'
            else:
                neighbors[i][j] = licznik
            if licznik < 4:
                SUM += 1

print(f'>>> ROLLS OF PAPER FOR ARRANGET: {SUM}')



