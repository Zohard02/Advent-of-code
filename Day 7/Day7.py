from collections import defaultdict

Directorios = defaultdict(int)
path =[]

for linea in open('D:/VisualStudioCode/CalendarioAdviento/Day 7/Input7.txt'):
    palabras = linea.split()
    if palabras[1] == 'cd':
        if palabras[2] == '..':
            path.pop()
        else:
            path.append(palabras[2])
    elif palabras[1] == 'ls':
        continue
    else:
        try:
            tamaño = int(palabras[0])
            for i in range(len(path) + 1):
                Directorios['/'.join(path[:i])] += tamaño
        except:
            pass

#Respuesta Parte 1:

p1 = 0
for k, v in Directorios.items():
    if v <= 100000:
        p1 += v

print(p1)

#Respuesta Parte 2:

maximo = 40000000
total_usado = Directorios['/']
liberar = total_usado - maximo
p2 = 1e9

for k, v in Directorios.items():
    if v >= liberar:
        p2 = min(p2, v)

print(p2)


