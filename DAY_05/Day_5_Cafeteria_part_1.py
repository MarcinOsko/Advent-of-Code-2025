
RANGE = []
PRODUCT = []
FRESH_PRODUCT = []

with open("Day_5_Cafeteria_input.txt", "r") as f:
    for line in f:
        if '-' in line.strip():
            RANGE.append(line.strip())
        else:
            if line.strip() != '':
                PRODUCT.append(line.strip())

for i in RANGE:
    rang = list(map(int, i.split('-')))
    for prod in PRODUCT:
        prod = int(prod)
        if rang[0] <= prod <= rang[1]:
            if not prod in FRESH_PRODUCT:
                FRESH_PRODUCT.append(prod)

print(f'>>> NUMBER FRESH INGREDIENS IS: {len(FRESH_PRODUCT)}')


