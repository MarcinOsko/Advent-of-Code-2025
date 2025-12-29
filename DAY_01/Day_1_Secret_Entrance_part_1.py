current_poz = 50
passwd = 0

with open("Day_1_Secret_Entrance_data.txt", "r") as f:
    for line in f:
        steps = int(line[1:])

        if current_poz == 0:
            passwd += 1
        if line[0] == "L":
            current_poz = (current_poz - steps) % 100
        else:
            current_poz = (current_poz + steps) % 100

print(f'>>> Result 2: {passwd}')
