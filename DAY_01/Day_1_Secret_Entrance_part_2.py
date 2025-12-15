
current_pos = 50
password = 0

with (open("Day_1_Secret_Entrance_data.txt", "r") as f):
    for line in f:
        steps = int(line[1:])
        if line[0] == "L":
            if current_pos == 0:
                hits = steps // 100
            else:
                move = current_pos - steps
                if move > 0:
                    hits = 0
                else:
                    hits = 1 + ((-move) // 100)
            password += hits
            current_pos = (current_pos - steps) % 100
        else:
            hits = (current_pos + steps) // 100
            password += hits
            current_pos = (current_pos + steps) % 100

print(f">>> PASWORD: {password}")