while True:
    try:
        qtdeListas = int(input())
    except EOFError:
        break

    listaNums = []  
    acc = 0         

    for _ in range(qtdeListas):
        listaNums.append(input())
    
    listaNums.sort()

    for i in range(len(listaNums)-1):
        prefixo = 0

        for j in range(len(listaNums[i])):
            if listaNums[i][j] == listaNums[i+1][j]:
                prefixo += 1
            else:
                break
            
        acc += prefixo
    print(acc)
