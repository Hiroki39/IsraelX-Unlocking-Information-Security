bases = []

for i in range(2, 13):
    modulos = set()
    curr = i
    isBase = True
    for j in range(1, 13):
        if curr % 13 in modulos:
            isBase = False
            break
        modulos.add(curr % 13)
        curr *= i
    if isBase:
        bases.append(i)

print(bases)
