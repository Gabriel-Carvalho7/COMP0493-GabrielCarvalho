casos = int(input())
listagem = {}

for _ in range(casos):
    tiposAlimentos = int(input())

    for _ in range(tiposAlimentos):
        tipo, peso = map(int, input().split())

        if tipo not in listagem:
            listagem[tipo] = []
        listagem[tipo].append(peso)

    acc = 0
    for valores in listagem.values():
        if all((num < 10 or num > 100) for num in valores):
            acc += max(valores)
        else:
            faixa = [num for num in valores if (num >= 10 and num <= 100)]
            acc += max(faixa)
    print(acc)
    listagem.clear()


