import math

class FenwickTree:
    def __init__(self, dados):
        self.tamanho = len(dados)
        self.arvore = [0] * (self.tamanho + 1) 
        self.construir(dados)
    
    def construir(self, dados):
        for i in range(self.tamanho):
            self.atualizar(i, dados[i])  
    
    def atualizar(self, indice, delta):
        i = indice + 1  
        while i <= self.tamanho:
            self.arvore[i] += delta
            i += i & -i  
    
    def consulta(self, indice):
        soma = 0
        i = indice + 1 
        while i > 0:
            soma += self.arvore[i]
            i -= i & -i  
        return soma

if __name__ == '__main__':
    dados = [1, 7, 3, 0, 7, 8, 3, 2, 6, 2]
    
    ft = FenwickTree(dados)
    print("Soma do prefixo até o índice 5:", ft.consulta(5))  
    ft.atualizar(3, 5)
    print("Após atualizar, soma do prefixo até o índice 5:", ft.consulta(5)) 