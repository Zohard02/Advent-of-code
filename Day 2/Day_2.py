with open('D:/VisualStudioCode/CalendarioAdviento/Day 2/Input2.txt') as lista:

    score = 0

    for e in lista:
        if (e == "A X\n"):
            score = score + 3
        elif (e == "A Y\n"):
            score = score + 4
        elif (e == "A Z\n"):
            score = score + 8
        elif (e == "B X\n"):
            score = score + 1
        elif (e == "B Y\n"):
            score = score + 5
        elif (e == "B Z\n"):
            score = score + 9
        elif (e == "C X\n"):
            score = score + 2
        elif (e == "C Y\n"):
            score = score + 6
        elif (e == "C Z\n"):
            score = score + 7

    print(score)

