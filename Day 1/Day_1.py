with open("D:/VisualStudioCode/CalendarioAdviento/Day 1/Input1.txt") as lis_calorias:

    calorias = []

    count = 0

    for e in lis_calorias:
        if (e == "\n"):
            calorias.append(count)
            count = 0
        else:
            count = count + int(e)

    calorias.sort()

    top_three = calorias[len(calorias) - 1] + calorias[len(calorias) - 2] + calorias[len(calorias) - 3]

    print(top_three)
