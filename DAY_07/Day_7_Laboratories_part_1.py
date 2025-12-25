
TREE_SOURCE = []
LINES = 0
COUNTER = 0

with open("Day_7_Laboratories_input.txt", "r") as f:
    for line in f:
        TREE_SOURCE.append(list(line.rstrip()))

LINES = len(TREE_SOURCE)

print(f'>>> SOURCE:')

for line in TREE_SOURCE:
    print(''.join(line))

print(f'\n>>> RESULT:')

for l in range(LINES):
    for c in range(len(TREE_SOURCE[l])):
        if TREE_SOURCE[l][c] == 'S':
            TREE_SOURCE[l+1][c] = '|'

        if TREE_SOURCE[l][c] == '^':
            TREE_SOURCE[l][c-1] = '|'
            TREE_SOURCE[l][c+1] = '|'
            if TREE_SOURCE[l+1][c-1] == '.':
                TREE_SOURCE[l+1][c-1] = '|'
            if TREE_SOURCE[l+1][c+1] == '.':
                TREE_SOURCE[l+1][c+1] = '|'
            if TREE_SOURCE[l][c] == '^' and TREE_SOURCE[l-1][c] == '|':
                COUNTER += 1

        if TREE_SOURCE[l][c] == '|' and l < len(TREE_SOURCE)-1:
            if TREE_SOURCE[l+1][c] == '.':
                TREE_SOURCE[l+1][c] = '|'
            if TREE_SOURCE[l+1][c] == '.':
                TREE_SOURCE[l+1][c] = '|'

for line in TREE_SOURCE:
    print(''.join(line))

print(f'\n>>> BEAM BE SPLIT {COUNTER} times')