class ConjuntoDisjunto:
    def __init__(self, tamanho):
        self.pai = list(range(tamanho))
        self.rank = [0] * tamanho
        self.num_componentes = tamanho

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x]) 
        return self.pai[x]

    def unir(self, x, y):
        raizX = self.encontrar(x)
        raizY = self.encontrar(y)
        if raizX == raizY:
            return False  
        
        if self.rank[raizX] < self.rank[raizY]:
            self.pai[raizX] = raizY
        else:
            self.pai[raizY] = raizX
            if self.rank[raizX] == self.rank[raizY]:
                self.rank[raizX] += 1
        self.num_componentes -= 1
        return True

def boruvka(numVertices, arestas):
    conjunto = ConjuntoDisjunto(numVertices)
    agm = [] 
    
    while conjunto.num_componentes > 1:
        maxAresta = {}  
        
        for u, v, peso in arestas:
            raizU = conjunto.encontrar(u)
            raizV = conjunto.encontrar(v)
            
            if raizU != raizV:
                if raizU not in maxAresta or peso > maxAresta[raizU][2]:
                    maxAresta[raizU] = (u, v, peso)
        
                if raizV not in maxAresta or peso > maxAresta[raizV][2]:
                    maxAresta[raizV] = (u, v, peso)
        
        adicionado = False
        for raiz in maxAresta:
            u, v, peso = maxAresta[raiz]
            if conjunto.encontrar(u) != conjunto.encontrar(v):
                agm.append((u, v, peso))
                conjunto.unir(u, v)
                adicionado = True
        
        if not adicionado:
            return None  
    
    return agm

if __name__ == "__main__":
    numVertices = 3
    arestas = [(0, 1, 1), (0, 2, 2), (1, 2, 3)]
    agm = boruvka(numVertices, arestas)
    
    print("Arestas da Árvore Geradora Máxima:")
    for aresta in agm:
        print(f"{aresta[0]} - {aresta[1]} (peso {aresta[2]})")