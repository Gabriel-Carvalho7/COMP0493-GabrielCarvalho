def problemaTroco(valor, moedas):
    sortedMoedas = sorted(moedas, reverse=True)
    
    troco = {}
    total = 0
    
    for moeda in sortedMoedas:
        if valor == 0:
            break  
        
        quantidade = valor // moeda
        
        if quantidade > 0:
            troco[moeda] = quantidade
            total += quantidade
            valor -= quantidade * moeda  
            
    if valor != 0:
        return "Não é possível dar o troco exato."
    
    return total, troco

if __name__ == "__main__":
    print(f"\nMoedas usadas: {problemaTroco(73, [25, 10, 5, 1])}\n")
