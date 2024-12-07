def tarefa1(arquivo):
    t = ""
    with open(arquivo, 'r') as f:
        for linha in f:
            linha = linha.strip()
            if linha.startswith("......."):
                break
            if t:
                t += " " + linha
            else:
                t = linha
    print(f"T: {t}")
    return t

def tarefa2(ttt, ppp):
    inicio = 0
    lista = []
    while True:
        find = ttt.find(ppp, inicio)
        if find == -1:
            if not lista:
                print("Saída: [-1]")
            else:
                print(f"Saída: {lista}")
            break
        lista.append(find)
        inicio = find + len(ppp)
    return lista

def tarefa3(ttt):
    vogais = "aeiou"
    digitos = vogais_count = consoantes_count = 0
    ttt_lower = ttt.lower() 

    for char in ttt_lower:
        if char.isdigit():
            digitos += 1
        elif char.isalpha():
            if char in vogais:
                vogais_count += 1
            else:
                consoantes_count += 1

    print(f"String em minúsculas: {ttt_lower}")
    print(f"Dígitos: {digitos}\nVogais: {vogais_count}\nConsoantes: {consoantes_count}")
    return digitos, vogais_count, consoantes_count

def tarefa4(ttt):
    delimitadores = " ."

    for delim in delimitadores:
        ttt = ttt.replace(delim, " ")

    tokens = ttt.lower().split()
    tokens.sort()
    menor_token = tokens[0] if tokens else None

    print(f"Tokens: {tokens}")
    print(f"Menor string lexicograficamente: {menor_token}")
    return tokens

def tarefa5(ttt):
    palavras = tarefa4(ttt)  
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    max_freq = max(contagem.values())
    mais_frequentes = [k for k, v in contagem.items() if v == max_freq]

    print(f"Palavras mais frequentes: {mais_frequentes}")
    return mais_frequentes

def tarefa6(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    ultima_linha = linhas[-1] if linhas else ""
    print(f"Última linha: {ultima_linha.strip()}")
    print(f"Quantidade de caracteres na última linha: {len(ultima_linha.strip())}")
    return len(ultima_linha.strip())

if __name__ == "__main__":
    arquivo = "entrada.txt"  
    ttt = input("Digite a string ttt: ")
    ppp = input("Digite a string ppp: ")

    print("\nTarefa 1:")
    #ttt = tarefa1(arquivo)

    print("\nTarefa 2:")
    tarefa2(ttt, ppp)

    print("\nTarefa 3:")
    tarefa3(ttt)

    print("\nTarefa 4:")
    tarefa4(ttt)
    
    print("\nTarefa 5:")
    tarefa5(ttt)
    
    print("\nTarefa 6:")
    #tarefa6(arquivo)
