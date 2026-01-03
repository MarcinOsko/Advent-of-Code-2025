import re
import pulp


def parse_line(line):
    targets = list(map(int, re.search(r'\{([^}]*)\}', line).group(1).split(',')))
    parts = re.findall(r'\(([^)]*)\)', line.split('{')[0])
    buttons = [
        list(map(int, p.split(','))) if p.strip() else []
        for p in parts
    ]
    return targets, buttons


def min_presses(targets, buttons):
    prob = pulp.LpProblem("Factory", pulp.LpMinimize)
    x = [
        pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer")
        for i in range(len(buttons))
    ]
    prob += pulp.lpSum(x)
    for i in range(len(targets)):
        prob += pulp.lpSum(
            x[j] for j, b in enumerate(buttons) if i in b
        ) == targets[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=False))
    return int(pulp.value(pulp.lpSum(x)))


total = 0
with open("Day_10_Factory_input.txt") as f:
    for line in f:
        targets, buttons = parse_line(line.strip())
        total += min_presses(targets, buttons)

print(total)
