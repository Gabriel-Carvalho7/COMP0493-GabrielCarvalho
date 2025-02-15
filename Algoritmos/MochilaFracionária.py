def mochilaFracionaria(itens, capacidade):
    itens.sort(key=lambda item: item[0] / item[1], reverse=True)
    
    total = 0.0
    pesoAtual = 0.0
    
    for valor, peso in itens:
        if pesoAtual + peso <= capacidade:
            total += valor
            pesoAtual += peso
        else:
            pesoRestante = capacidade - pesoAtual
            total += valor * (pesoRestante / peso)
            pesoAtual = capacidade
            break  
    
    return total

print(f"\nMochila Fracionária: {mochilaFracionaria([(60, 10), (100, 20), (120, 30)], 50)}\n")
