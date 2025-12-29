numbers_lists = []
work_numbers_lists = []
sum_all = 0

with open("Day_6_Trash_Compactor_input.txt", "r") as f:
    for line in f:
        numbers_lists.append(list(line.rstrip()))

longest_row = max(numbers_lists, key=len)
lenght_row = len(longest_row)
numbers_col = len(numbers_lists[0])

def list_to_number(lst):
    return int(''.join(x.strip() for x in lst if x.strip()))

for number in numbers_lists:
    if len(number) < len(longest_row):
        number.extend([" "] * (len(longest_row) - len(number)))
    work_numbers_lists.append(number)
    print(number)
numbers_row = len(work_numbers_lists)

temp = []
math = []
oprt = ''
break_column = False
count_break = 0
for i in reversed(range(numbers_col)):
    for j in range(numbers_row):
        item = work_numbers_lists[j][i]
        if item != '+' and item != '*':
            temp.append(item)
            if item == ' ':
                count_break += 1
        else:
            oprt += item
    if count_break == numbers_row:
        break_column = True
    if not break_column:
        temp = [x.strip() for x in temp if x.strip()]
        temp = ''.join(temp)
        temp = int(temp)
        math.append(temp)
    if '+' in oprt:
        sum_all += sum(math)
        math = []
    if '*' in oprt:
        mn = 1
        for x in math:
            mn *= x
        sum_all += mn
        math = []
    break_column = False
    count_break = 0
    temp = []
    oprt = ''

print(f'>>> SUM OF CEPHALOPOD MATH: {sum_all}')
