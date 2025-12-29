ranges_source = []
ranges = []

with (open("Day_5_Cafeteria_input.txt", "r") as f):
    for line in f:
        if '-' in line.strip():
            ranges_source.append(line.strip())

ranges = [tuple(map(int, r.split('-'))) for r in ranges_source]

def ranges_of_fresh(ranges):
    ranges.sort()

    total = 0
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start > current_end + 1:
            total += current_end - current_start + 1
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)

    total += current_end - current_start + 1
    return total

print(f'>>> NUMBER FRESH INGREDIENS IS: {ranges_of_fresh(ranges)}')
