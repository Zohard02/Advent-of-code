lista = open('Input6.txt').read()

#ORIGINAL:
for x in range(len(lista)):
    if x-3 >= 0 and len(set([lista[x], lista[x-1], lista[x-2], lista[x-3]])) == 4:
        print(x+1)
        break
        


#PARTE 1:
encontrado = False
for x in range(len(lista)):
    if not(encontrado) and x-3 >= 0 and len(set([lista[x-y] for y in range(4)])) == 4:
        print(x+1)
        encontrado = True
  

#PARTE 2:
encontrado = False
for x in range(len(lista)):
    if encontrado != True and x-13 >= 0 and len(set([lista[x-y] for y in range(14)])) == 14:
        print(x+1)
        encontrado = True