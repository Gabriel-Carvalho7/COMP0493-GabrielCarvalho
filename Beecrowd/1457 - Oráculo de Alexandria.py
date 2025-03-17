count = int(input())

def contaRep(valor, acc, rep):
    if (valor - acc*rep) < 1:
        return 1
    return (valor - acc*rep) * contaRep(valor, acc+1, rep)

while count > 0:
    dado = input()
    rep = dado.count('!')
    if dado[0:3].isdigit():
        valor = int(dado[0:3])
    elif dado[0:2].isdigit():
        valor = int(dado[0:2])
    else:
        valor = int(dado[0])
    print(contaRep(valor, 0, rep))
    count -= 1


    