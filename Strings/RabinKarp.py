def rabin_karp_busca(texto, padrao):
    if not padrao or not texto or len(padrao) > len(texto):
        return []
    
    n = len(texto)
    m = len(padrao)
    base = 256
    q = 101  
    h = 1
    for i in range(m - 1):
        h = (h * base) % q
    hash_padrao = 0
    hash_texto = 0
    
    for i in range(m):
        hash_padrao = (base * hash_padrao + ord(padrao[i])) % q
        hash_texto = (base * hash_texto + ord(texto[i])) % q
        
    ocorrencias = []
    for i in range(n - m + 1):
        if hash_padrao == hash_texto:
            if texto[i:i+m] == padrao:
                ocorrencias.append(i)
        if i < n - m:
            hash_texto = (base * (hash_texto - ord(texto[i]) * h) + ord(texto[i + m])) % q
            if hash_texto < 0:
                hash_texto += q
    return ocorrencias

if __name__ == '__main__':
    texto = "GEEKS FOR GEEKS"
    padrao = "GEEK"
    print("Texto:", texto)
    print("Padrão:", padrao)
    posicoes = rabin_karp_busca(texto, padrao)
    print("Ocorrências do padrão:", posicoes)
