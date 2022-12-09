#PARTE 1
inicial = [[],
    ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R'],
    ['J', 'Z', 'P', 'D', 'F', 'S', 'H'],
    ['V', 'H', 'Z'],
    ['H', 'G', 'F', 'J', 'Z', 'M'],
    ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T'],
    ['J', 'Z', 'H', 'V', 'W', 'T', 'M'],
    ['Z', 'L', 'P', 'F', 'T'],
    ['S', 'W', 'V', 'Q'],
    ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']]

for orden in open('Input5.txt'):
    palabras = orden.split()
    cuanto = int(palabras[1])
    de = int(palabras[3])
    a = int(palabras[5])
    mover = inicial[de][:cuanto]
    inicial[de] = inicial[de][cuanto:]
    inicial[a] = list(reversed(mover)) + inicial[a]

print(''.join([i[0] for i in inicial if len(i)>0]))


#PARTE 2
inicial = [[],
    ['N', 'T', 'B', 'S', 'Q', 'H', 'G', 'R'],
    ['J', 'Z', 'P', 'D', 'F', 'S', 'H'],
    ['V', 'H', 'Z'],
    ['H', 'G', 'F', 'J', 'Z', 'M'],
    ['R', 'S', 'M', 'L', 'D', 'C', 'Z', 'T'],
    ['J', 'Z', 'H', 'V', 'W', 'T', 'M'],
    ['Z', 'L', 'P', 'F', 'T'],
    ['S', 'W', 'V', 'Q'],
    ['C', 'N', 'D', 'T', 'M', 'L', 'H', 'W']]

for orden in open('Input5.txt'):
    palabras = orden.split()
    cuanto = int(palabras[1])
    de = int(palabras[3])
    a = int(palabras[5])
    mover = inicial[de][:cuanto]
    inicial[de] = inicial[de][cuanto:]
    inicial[a] = mover + inicial[a]

print(''.join([i[0] for i in inicial if len(i)>0]))