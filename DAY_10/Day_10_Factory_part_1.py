from itertools import combinations

input = []
sum = 0

with open("Day_10_Factory_input.txt", "r") as f:
    for l in f:
        input.append(l.rsplit())

for line in input:
    lamps = ""
    keys = []
    electric = []

    for item in line:
        if item.startswith('[') and item.endswith(']'):
            lamps = item[1:-1]
        elif item.startswith('(') and item.endswith(')'):
            content = item[1:-1]
            if ',' in content:
                keys.append(tuple(map(int, content.split(','))))
            else:
                keys.append((int(content),))
        elif item.startswith('{') and item.endswith('}'):
            electric = list(map(int, item[1:-1].split(',')))

    goal = lamps
    buttons = keys
    start = str('.' * len(lamps))

    start_bits = [0 if c == '.' else 1 for c in start]
    print("Start bits:", type(start_bits), start_bits)
    goal_bits = [0 if c == '.' else 1 for c in goal]
    print("Goal bits:", type(goal_bits), goal_bits)

    print("Lamps:", lamps)
    print("Keys:", keys)
    print("Electric:", electric)
    print(100 * '-')

    n_buttons = len(buttons)

    def press_buttons(combo):
        state = start_bits.copy()
        for i in combo:
            for idx in buttons[i]:
                state[idx] ^= 1
        return state

    solution = None
    for r in range(1, n_buttons + 1):
        for combo in combinations(range(n_buttons), r):
            if press_buttons(combo) == goal_bits:
                solution = combo
                break
        if solution is not None:
            break

    if solution is not None:
        sum += len(solution)
        print(">>> You have to press the buttons with the indexes:", solution)
        print(100 * '-', '\n\n')
    else:
        print("No solution")

print(30*'*')
print("* Sum of button presses:", sum)
print(30*'*')