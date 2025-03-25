import heapq

def a_estrela(grafo, inicio, objetivo, heuristica):
    prioridade = []
    heapq.heappush(prioridade, (0, inicio))
    
    veioDe = {inicio: None}
    gScore = {no: float('inf') for no in grafo}
    gScore[inicio] = 0
    fScore = {no: float('inf') for no in grafo}
    fScore[inicio] = heuristica(inicio, objetivo)

    while prioridade:
        atual = heapq.heappop(prioridade)[1]

        if atual == objetivo:
            return reconstruir(veioDe, atual)

        for vizinho in grafo[atual]['vizinhos']:
            custoTentativa = gScore[atual] + grafo[atual]['vizinhos'][vizinho]
            
            if custoTentativa < gScore[vizinho]:
                veioDe[vizinho] = atual
                gScore[vizinho] = custoTentativa
                fScore[vizinho] = custoTentativa + heuristica(vizinho, objetivo)
                heapq.heappush(prioridade, (fScore[vizinho], vizinho))
    
    return None 

def reconstruir(veioDe, atual):
    caminho = []
    while atual is not None:
        caminho.append(atual)
        atual = veioDe[atual]
    return caminho[::-1]

def heuristicaManhattan(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)

grafo = {
    (0,0): {'vizinhos': {(0,1): 1, (1,0): 1}, 'bloqueado': False},
    (0,1): {'vizinhos': {(0,0): 1, (1,1): 1}, 'bloqueado': False},
    (1,0): {'vizinhos': {(0,0): 1, (1,1): 1}, 'bloqueado': False},
    (1,1): {'vizinhos': {(0,1): 1, (1,0): 1, (2,1): 1}, 'bloqueado': False},
    (2,1): {'vizinhos': {(1,1): 1, (2,2): 1}, 'bloqueado': False},
    (2,2): {'vizinhos': {(2,1): 1}, 'bloqueado': False}
}

caminho = a_estrela(
    grafo = grafo,
    inicio = (0,0),
    objetivo = (2,2),
    heuristica = heuristicaManhattan
)

print("Caminho encontrado:", caminho)