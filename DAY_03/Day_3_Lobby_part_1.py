with open("Day_3_Lobby_input.txt", "r") as f:
    lines = f.readlines()

digits = []
SUM = 0

for line in lines:
    line = line.strip()
    for digit in line:
        digits.append(int(digit))

    tmp_digits = digits.copy()
    tmp_digits.pop(len(digits) - 1)
    max1 = max(tmp_digits)
    max1_index = digits.index(max1)
    for n in range(max1_index + 1):
        digits.pop(0)
    max2 = max(digits)
    digits = []

    result_digits = (max1, max2)
    result_digits = int(''.join(map(str, result_digits)))
    SUM += result_digits

print(f'>>> TOTAL OUTPUT JOLTAGE: {SUM}')
