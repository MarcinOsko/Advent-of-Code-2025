range = []
product = []
fresh_product = []

with open("Day_5_Cafeteria_input.txt", "r") as f:
    for line in f:
        if '-' in line.strip():
            range.append(line.strip())
        else:
            if line.strip() != '':
                product.append(line.strip())

for i in range:
    rang = list(map(int, i.split('-')))
    for prod in product:
        prod = int(prod)
        if rang[0] <= prod <= rang[1]:
            if not prod in fresh_product:
                fresh_product.append(prod)

print(f'>>> NUMBER FRESH INGREDIENS IS: {len(fresh_product)}')
