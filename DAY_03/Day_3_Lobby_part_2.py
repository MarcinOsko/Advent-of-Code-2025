sum_all = 0

with open("Day_3_Lobby_input.txt", "r") as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()

        stack = []
        for_cut = len(line) - 12

        for c in line:
            while stack and for_cut > 0 and stack[-1] < c:
                stack.pop()
                for_cut -= 1
            stack.append(c)

        result = int("".join(stack[:12]))
        sum_all += result

print(f'>>> TOTAL OUTPUT JOLTAGE: {sum_all}')
