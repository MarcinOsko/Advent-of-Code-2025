grid = []
grid_temp = []
sum = 0
directions = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

with open("Day_4_Printing_Department_input.txt", "r") as f:
    for line in f:
        grid.append(line.strip())

print(grid)

grid_lines = len(grid)
grid_fields = len(grid[0])
if grid_lines == grid_fields:
    N = grid_lines

neighbors = [['.'] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        counter = 0
        if grid[i][j] == '@':
            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    if grid[ni][nj] == '.':
                        neighbors[ni][nj] = '.'
                    if grid[ni][nj] == '@':
                        counter += 1
            if counter < 4:
                neighbors[i][j] = '.'
                sum += 1
            if counter >= 4:
                neighbors[i][j] = '@'
    new_grid_line = neighbors[i]
    new_grid_line = ''.join(new_grid_line)
    grid_temp.append(new_grid_line)
print(grid_temp)

while True:
    grid = []
    grid = grid_temp
    grid_temp = []

    grid_lines = len(grid)
    grid_fields = len(grid[0])
    if grid_lines == grid_fields:
        N = grid_lines

    neighbors = [['.'] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            counter = 0
            if grid[i][j] == '@':
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N:
                        if grid[ni][nj] == '.':
                            neighbors[ni][nj] = '.'
                        if grid[ni][nj] == '@':
                            counter += 1
                if counter < 4:
                    neighbors[i][j] = '.'
                    sum += 1
                if counter >= 4:
                    neighbors[i][j] = '@'
        new_grid_line = neighbors[i]
        new_grid_line = ''.join(new_grid_line)
        grid_temp.append(new_grid_line)
    if grid_temp == grid:
        break
    print(grid_temp)

print(f'>>> ROLLS OF PAPER FOR ARRANGET: {sum}')
