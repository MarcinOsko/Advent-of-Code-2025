
with open("Day_1_Secret_Entrance_data.txt") as file:
    numbers = file.readlines()

current_point = 50
result = 0

for code in numbers:
    steps = int(code[1:])
    start = current_point

    full_around = steps // 100
    result += full_around
    rem = steps % 100

    if code[0] == 'R':
        end = (start + rem) % 100
        if rem > 0 and end < start:
            result += 1
        current_point = end

    elif code[0] == 'L':
        end = (start - rem) % 100
        if rem > 0 and end > start:
            result += 1
        current_point = end


print(f'>>> Result 2: {result}')

