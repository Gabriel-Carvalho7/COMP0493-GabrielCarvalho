def preproc_bad(padrao):
    tabela = {}
    for i, c in enumerate(padrao):
        tabela[c] = i
    return tabela

def preproc_good(padrao):
    m = len(padrao)
    shift = [0] * (m + 1)
    border = [0] * (m + 1)
    i, j = m, m + 1
    border[i] = j
    while i > 0:
        while j <= m and padrao[i - 1] != padrao[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border[j]
        i -= 1
        j -= 1
        border[i] = j
    j = border[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border[j]
    return shift

def boyerBusca(texto, padrao):
    if not padrao:
        return []
    bad = preproc_bad(padrao)
    good = preproc_good(padrao)
    m, n = len(padrao), len(texto)
    ocorrencias = []
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and padrao[j] == texto[s + j]:
            j -= 1
        if j < 0:
            ocorrencias.append(s)
            s += good[0]
        else:
            bc = j - bad.get(texto[s + j], -1)
            gs = good[j + 1]
            s += max(bc, gs)
    return ocorrencias

if __name__ == '__main__':
    texto = "ABAAABCD"
    padrao = "ABC"
    print("Texto:", texto)
    print("Padrão:", padrao)
    print("Ocorrências:", boyerBusca(texto, padrao))
