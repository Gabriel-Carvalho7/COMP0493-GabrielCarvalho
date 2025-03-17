from collections import defaultdict

class Grafo:
    def __init__(self, vertices):
        self.grafo = defaultdict(lambda: defaultdict(int))  
        self.V = vertices 

    def adicionar_aresta(self, u, v, capacidade):
        self.grafo[u][v] = capacidade  

    def _busca_em_profundidade(self, origem, destino, pai):
        visitados = set()
        pilha = [origem]
        pai.clear()

        while pilha:
            u = pilha.pop()
            if u in visitados:
                continue
            visitados.add(u)

            for v in self.grafo[u]:  
                capacidade = self.grafo[u][v]
                if capacidade > 0 and v not in visitados:
                    pai[v] = u
                    if v == destino:
                        return True
                    pilha.append(v)
        return False

    def ford_fulkerson(self, origem, destino):
        fluxo_maximo = 0

        while True:
            pai = {}
            encontrou_caminho = self._busca_em_profundidade(origem, destino, pai)
            if not encontrou_caminho:
                break

            fluxo_caminho = float('Inf')
            v = destino
            while v != origem:
                u = pai[v]
                fluxo_caminho = min(fluxo_caminho, self.grafo[u][v])
                v = u

            v = destino
            while v != origem:
                u = pai[v]
                self.grafo[u][v] -= fluxo_caminho
                self.grafo[v][u] += fluxo_caminho 
                v = u

            fluxo_maximo += fluxo_caminho

        return fluxo_maximo

# Exemplo de uso
g = Grafo(6)
g.adicionar_aresta(0, 1, 16)
g.adicionar_aresta(0, 2, 13)
g.adicionar_aresta(1, 2, 10)
g.adicionar_aresta(1, 3, 12)
g.adicionar_aresta(2, 1, 4)
g.adicionar_aresta(2, 4, 14)
g.adicionar_aresta(3, 2, 9)
g.adicionar_aresta(3, 5, 20)
g.adicionar_aresta(4, 3, 7)
g.adicionar_aresta(4, 5, 4)

origem, destino = 0, 5
print("O fluxo máximo é", g.ford_fulkerson(origem, destino))