def calcularPrefixo(padrao):
    tabela = [0] * len(padrao)
    k = 0
    for i in range(1, len(padrao)):
        while k > 0 and padrao[k] != padrao[i]:
            k = tabela[k - 1]
        if padrao[k] == padrao[i]:
            k += 1
        tabela[i] = k
    return tabela

def buscaKMP(texto, padrao):
    ocorrencias = []
    tabelaPrefixo = calcularPrefixo(padrao)
    q = 0
    for i in range(len(texto)):
        while q > 0 and padrao[q] != texto[i]:
            q = tabelaPrefixo[q - 1]
        if padrao[q] == texto[i]:
            q += 1
        if q == len(padrao):
            ocorrencias.append(i - len(padrao) + 1)
            q = tabelaPrefixo[q - 1]
    return ocorrencias

if __name__ == '__main__':
    texto = "ABABDABACDABABCABAB"
    padrao = "BABCAB"
    
    print("Texto: ", texto)
    print("Padrão: ", padrao)
    
    posicoes = buscaKMP(texto, padrao)
    if posicoes:
        print("Padrão encontrado nas posições:", posicoes)
    else:
        print("Padrão não encontrado no texto.")
