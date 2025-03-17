while True:
    valores = input()
    valores = valores.split()
    valores = [int(x) for x in valores]

    if all(valor == 0 for valor in valores):
        break

    lista = []

    for i in range(valores[0]):
        linha = input()
        lista.append(linha)

    valores2 = input()
    valores2 = valores2.split()
    valores2 = [int(x) for x in valores2]

    repL = int(valores2[0] / valores[0])
    repC = int(valores2[1] / valores[1])

    for str in lista:
        for i in range(repL):
            for char in str:
                print(f"{char * repC}", end='')
            print()
    print()
    


