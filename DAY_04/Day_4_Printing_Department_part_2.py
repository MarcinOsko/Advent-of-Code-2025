
GRID = []
GRID_TEMP = []
SUM = 0
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0,-1), (0,1),
              (1,-1), (1,0), (1,1)]

with open("Day_4_Printing_Department_input.txt", "r") as f:
    for line in f:
        GRID.append(line.strip())

print(GRID)

grid_lines = len(GRID)
grid_fields = len(GRID[0])
if grid_lines == grid_fields:
    N = grid_lines

neighbors = [['.']*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        counter = 0
        if GRID[i][j] == '@':
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N:
                    if GRID[ni][nj] == '.':
                        neighbors[ni][nj] = '.'
                    if GRID[ni][nj] == '@':
                        counter += 1
            if counter < 4:
                neighbors[i][j] = '.'
                SUM += 1
            if counter >= 4:
                neighbors[i][j] = '@'
    new_grid_line = neighbors[i]
    new_grid_line = ''.join(new_grid_line)
    GRID_TEMP.append(new_grid_line)
print(GRID_TEMP)


while True:
    GRID = []
    GRID = GRID_TEMP
    GRID_TEMP = []

    grid_lines = len(GRID)
    grid_fields = len(GRID[0])
    if grid_lines == grid_fields:
        N = grid_lines

    neighbors = [['.']*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            counter = 0
            if GRID[i][j] == '@':
                for dx, dy in DIRECTIONS:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < N and 0 <= nj < N:
                        if GRID[ni][nj] == '.':
                            neighbors[ni][nj] = '.'
                        if GRID[ni][nj] == '@':
                            counter += 1
                if counter < 4:
                    neighbors[i][j] = '.'
                    SUM += 1
                if counter >= 4:
                    neighbors[i][j] = '@'
        new_grid_line = neighbors[i]
        new_grid_line = ''.join(new_grid_line)
        GRID_TEMP.append(new_grid_line)
    if GRID_TEMP == GRID:
        break
    print(GRID_TEMP)

print(f'>>> ROLLS OF PAPER FOR ARRANGET: {SUM}')