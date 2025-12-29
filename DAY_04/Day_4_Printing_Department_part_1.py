grid = []
sum_all = 0
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

with open("Day_4_Printing_Department_input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

grid_lines = len(grid)
grid_fields = len(grid[0])
if grid_lines == grid_fields:
    N = grid_lines

neighbors = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        licznik = 0
        if grid[i][j] == '@':
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    if grid[ni][nj] == '@':
                        licznik += 1
            if licznik < 4:
                neighbors[i][j] = 'x'
            else:
                neighbors[i][j] = licznik
            if licznik < 4:
                sum_all += 1

print(f'>>> ROLLS OF PAPER FOR ARRANGET: {sum_all}')
