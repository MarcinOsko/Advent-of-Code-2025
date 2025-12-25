import math

NUMBERS_LISTS = []
WORK_NUMBERS_LISTS = []
SUM = 0

with open("Day_6_Trash_Compactor_input.txt", "r") as f:
    for line in f:
        NUMBERS_LISTS.append(list(line.rstrip()))

longest_row = max(NUMBERS_LISTS, key=len)
LENGHT_ROW = len(longest_row)
NUMBERS_COL = len(NUMBERS_LISTS[0])

def list_to_number(lst):
    return int(''.join(x.strip() for x in lst if x.strip()))

for number in NUMBERS_LISTS:
    if len(number) < len(longest_row):
        number.extend([" "] * (len(longest_row) - len(number)))
    WORK_NUMBERS_LISTS.append(number)
    print(number)
NUMBERS_ROW = len(WORK_NUMBERS_LISTS)

temp = []
math = []
oprt = ''
break_column = False
count_break = 0
for i in reversed(range(NUMBERS_COL)):
    for j in range(NUMBERS_ROW):
        item = WORK_NUMBERS_LISTS[j][i]
        if item != '+' and item != '*':
            temp.append(item)
            if item == ' ':
                count_break += 1
        else:
            oprt += item
    if count_break == NUMBERS_ROW:
        break_column = True
    if not break_column:
        temp = [x.strip() for x in temp if x.strip()]
        temp = ''.join(temp)
        temp = int(temp)
        math.append(temp)
    if '+' in oprt:
        SUM += sum(math)
        math = []
    if '*' in oprt:
        mn = 1
        for x in math:
            mn *= x
        SUM += mn
        math = []
    break_column = False
    count_break = 0
    temp = []
    oprt = ''

print(f'>>> SUM OF CEPHALOPOD MATH: {SUM}')

