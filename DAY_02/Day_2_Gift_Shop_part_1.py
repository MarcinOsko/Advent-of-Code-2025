with open("Day_2_Gift_Shop_input.txt", "r") as f:
    SUM = 0
    for rangeStr in f.read().split(','):
        start, end = map(int, rangeStr.split('-'))
        for num in range(start, end + 1):
            num_str = str(num)
            if len(str(num)) % 2 == 0:
                if num_str[:len(str(num)) // 2] == num_str[len(str(num)) // 2:]:
                    SUM += num
print(f'>>> SUM: {SUM}')
