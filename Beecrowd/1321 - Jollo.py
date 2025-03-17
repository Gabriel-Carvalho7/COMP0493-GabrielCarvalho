while True:
    a, b, c, x, y = map(int, input().split())

    if (a+b+c+x+y) == 0:
        break

    princesa = [a, b, c]
    princesa = sorted(princesa)
    principe = [x, y]
    todas = [a, b, c, x, y]
    
    winX = len([num for num in princesa if x > num])
    winY = len([num for num in princesa if y > num])

    if (winX + winY) < 3 or (winX == 1 and winY == 2) or (winX == 2 and winY == 1):
        print("-1")
    elif (winX + winY) == 3 or (winX == 1 and winY == 3) or (winX == 3 and winY == 1):
        for i in range(0, 6):
            if (max(princesa) + i) in todas:
                continue
            else:
                if (max(princesa) + i) > 52:
                    print("-1")
                    break
                print(max(princesa) + i)
                break
    
    elif (winX + winY) == 6:
        for i in range(1, 6):
            if i in todas:
                continue
            else:
                print(i)
                break

    else:
        for i in range(0, 6):
            if (princesa[1] + i) in todas:
                continue
            else:
                if (princesa[1] + i) > 52:
                    print("-1")
                    break
                print(princesa[1] + i)
                break
