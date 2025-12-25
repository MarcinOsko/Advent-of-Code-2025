
number_lists = []
SUM = 0

with open("Day_6_Trash_Compactor_input.txt", "r") as f:
    for line in f:
        number_lists.append(line.split())

for n in range(len(number_lists[0])):
    if number_lists[4][n] == '*':
        x = int(number_lists[0][n]) * int(number_lists[1][n]) * int(number_lists[2][n]) * int(number_lists[3][n])
        SUM += x
    if number_lists[4][n] == '+':
        x = int(number_lists[0][n]) + int(number_lists[1][n]) + int(number_lists[2][n]) + int(number_lists[3][n])
        SUM += x

print(f'>>> SUM OF CEPHALOPOD MATH: {SUM}')

