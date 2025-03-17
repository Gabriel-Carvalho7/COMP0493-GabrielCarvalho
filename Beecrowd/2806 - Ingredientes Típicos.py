from math import ceil
from collections import defaultdict

# Função para determinar se uma porção é típica
def is_typical(porcao, listagem, ingredientes_tipicos, cache):
    # Verificar se já foi calculado
    if porcao in cache:
        return cache[porcao]

    # Obter componentes da porção
    componentes = listagem.get(porcao, [])
    tipicos_count = 0
    total_count = len(componentes)

    # Verificar os componentes
    for componente in componentes:
        if componente in ingredientes_tipicos:
            # Componente é um ingrediente típico
            tipicos_count += 1
        elif componente in listagem:
            # Componente é outra porção; verificar recursivamente
            if is_typical(componente, listagem, ingredientes_tipicos, cache):
                tipicos_count += 1

    # Determinar se a porção é típica
    resultado = tipicos_count > total_count // 2
    cache[porcao] = resultado
    return resultado

# Entrada
N = int(input().strip())  # Número de ingredientes típicos
ingredientes_tipicos = set(input().strip().split())  # Ingredientes típicos em uma única linha

M = int(input().strip())  # Número de porções
listagem = defaultdict(list)

# Lendo as porções
for _ in range(M):
    linha1 = input().strip().split()
    nome_porcao = linha1[0]
    K = int(linha1[1])  # Número de componentes
    componentes = input().strip().split()  # Componentes em uma única linha
    listagem[nome_porcao] = componentes

# Avaliar cada porção
cache = {}
for porcao in listagem:
    if is_typical(porcao, listagem, ingredientes_tipicos, cache):
        print("porcao tipica")
    else:
        print("porcao comum")
