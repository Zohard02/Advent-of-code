parte1 = 0

for linea in open('Input4.txt'):
    p1, p2 = linea.split(',')
    n1, n2 = p1.split('-')
    n3, n4 = p2.split('-')
    n1, n2, n3, n4 = [int(x) for x in [n1, n2, n3, n4]]
    if (n1 <= n3 and n4 <= n2) or (n3 <= n1 and n2 <= n4):
        parte1 += 1

print(parte1)

parte2 = 0

for linea in open('Input4.txt'):
    p1, p2 = linea.split(',')
    n1, n2 = p1.split('-')
    n3, n4 = p2.split('-')
    n1, n2, n3, n4 = [int(x) for x in [n1, n2, n3, n4]]
    #  n2     |       n1 
    #       n3| n4
    if not(n2 < n3 or n1 > n4):
        parte2 += 1

print(parte2)