current_pos = 50
password = 0

with (open("Day_1_Secret_Entrance_data.txt", "r") as f):
    for line in f:
        steps = int(line[1:])
        if line[0] == "L":
            if current_pos == 0:
                hit = steps // 100
            else:
                move = current_pos - steps
                if move > 0:
                    hit = 0
                else:
                    hit = 1 + ((-move) // 100)
            password += hit
            current_pos = (current_pos - steps) % 100
        else:
            hit = (current_pos + steps) // 100
            password += hit
            current_pos = (current_pos + steps) % 100

print(f">>> PASWORD: {password}")
