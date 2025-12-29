tree_source = []
lines = 0
counter = 0

with open("Day_7_Laboratories_input.txt", "r") as f:
    for line in f:
        tree_source.append(list(line.rstrip()))

lines = len(tree_source)

print(f'>>> SOURCE:')

for line in tree_source:
    print(''.join(line))

print(f'\n>>> RESULT:')

for l in range(lines):
    for c in range(len(tree_source[l])):
        if tree_source[l][c] == 'S':
            tree_source[l + 1][c] = '|'

        if tree_source[l][c] == '^':
            tree_source[l][c - 1] = '|'
            tree_source[l][c + 1] = '|'
            if tree_source[l + 1][c - 1] == '.':
                tree_source[l + 1][c - 1] = '|'
            if tree_source[l + 1][c + 1] == '.':
                tree_source[l + 1][c + 1] = '|'
            if tree_source[l][c] == '^' and tree_source[l - 1][c] == '|':
                counter += 1

        if tree_source[l][c] == '|' and l < len(tree_source) - 1:
            if tree_source[l + 1][c] == '.':
                tree_source[l + 1][c] = '|'
            if tree_source[l + 1][c] == '.':
                tree_source[l + 1][c] = '|'

for line in tree_source:
    print(''.join(line))

print(f'\n>>> BEAM BE SPLIT {counter} times')
