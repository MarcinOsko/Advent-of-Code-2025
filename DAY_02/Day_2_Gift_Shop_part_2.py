with open("Day_2_Gift_Shop_input.txt", "r") as f:
    SUM = 0
    for rangeStr in f.read().split(','):
        start, end = rangeStr.split('-')[0], rangeStr.split('-')[1]
        for num in range(int(start), int(end) + 1):
            num_str = str(num)
            if len(str(num)) > 1:
                if len(str(num)) > 1:
                    for pat_len in range(1, len(str(num)) // 2 + 1):
                        if len(str(num)) % pat_len == 0:
                            pattern = num_str[:pat_len]
                            repeats = len(str(num)) // pat_len
                            if pattern * repeats == num_str:
                                SUM += num
                                break

print(f">>> PASWORD: {SUM}")
