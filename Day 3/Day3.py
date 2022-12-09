parte1 = 0
for linea in open('Input3.txt'):
    rucksack = linea.strip()
    first = rucksack[:len(rucksack)//2]
    second = rucksack[len(rucksack)//2:]

    for x in first:
        if x in second:
            if 'a' <= x <= 'z':
                parte1 += ord(x) - ord('a') + 1
            else:
                parte1 += ord(x) - ord('A') + 27
            break

print(parte1)

parte2 = 0

group = [line for line in open("Input3.txt")]

i = 0

while i < len(group):
    for x in group[i]:
        if x in group[i+1] and x in group[i+2]:
            if 'a' <= x <= 'z':
                parte2 += ord(x) - ord('a') + 1
            else:
                parte2 += ord(x) - ord('A') + 27
            break
    i += 3

print(parte2)