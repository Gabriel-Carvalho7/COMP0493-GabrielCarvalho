import heapq


class UnionFind:
    def __init__(self, tamanho):
        self.pai = list(range(tamanho))
        self.altura = [0] * tamanho

    def encontrar(self, x):
        if self.pai[x] != x:
            self.pai[x] = self.encontrar(self.pai[x])
        return self.pai[x]

    def unir(self, x, y):
        raizX = self.encontrar(x)
        raizY = self.encontrar(y)
        if raizX == raizY:
            return False
        if self.altura[raizX] > self.altura[raizY]:
            self.pai[raizY] = raizX
        else:
            self.pai[raizX] = raizY
            if self.altura[raizX] == self.altura[raizY]:
                self.altura[raizY] += 1
        return True

def kruskal(arestas, numNos):
    conj = UnionFind(numNos)
    arestas = sorted(arestas, key=lambda x: x[2])
    agm = []
    pesoTotal = 0
    for aresta in arestas:
        u, v, peso = aresta
        if conj.encontrar(u) != conj.encontrar(v):
            conj.unir(u, v)
            agm.append((u, v, peso))
            pesoTotal += peso
    return pesoTotal, agm

def prim(listaAdjacencia, numNos):
    visitado = [False] * numNos
    fila = []
    agm = []
    pesoTotal = 0
    visitado[0] = True
    for vizinho, peso in listaAdjacencia[0]:
        heapq.heappush(fila, (peso, 0, vizinho))
    while fila and len(agm) < numNos - 1:
        peso, u, v = heapq.heappop(fila)
        if not visitado[v]:
            visitado[v] = True
            agm.append((u, v, peso))
            pesoTotal += peso
            for vizinho, p in listaAdjacencia[v]:
                if not visitado[vizinho]:
                    heapq.heappush(fila, (p, v, vizinho))
    return pesoTotal, agm

arestas = [
    (0, 1, 10), (0, 2, 6), (0, 3, 5),
    (1, 3, 15), (2, 3, 4)
]

numNos = 4
listaAdjacencia = [[] for _ in range(numNos)]
for u, v, peso in arestas:
    listaAdjacencia[u].append((v, peso))
    listaAdjacencia[v].append((u, peso))

pesoKruskal, amgKruskal = kruskal(arestas, numNos)
print("Kruskal - Peso total:", pesoKruskal)
print("Arestas da AGM:", amgKruskal)

pesoPrim, agmPrim = prim(listaAdjacencia, numNos)
print("\nPrim - Peso total:", pesoPrim)
print("Arestas da AGM:", agmPrim)
