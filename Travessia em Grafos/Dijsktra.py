import heapq

def dijkstra(grafo, inicio):
    distancias = {no: float('infinity') for no in grafo}
    distancias[inicio] = 0

    fila = [(0, inicio)]
    
    while fila:
        distancia_atual, no_atual = heapq.heappop(fila)
        
        if distancia_atual > distancias[no_atual]:
            continue
        
        for vizinho, peso in grafo[no_atual]:
            distancia = distancia_atual + peso
            
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(fila, (distancia, vizinho))
    
    return distancias

grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('B', 2), ('D', 1)],
    'D': [('C', 1), ('B', 5)]
}

distancias = dijkstra(grafo, 'A')
print("Distâncias mais curtas a partir de A:")
for no, distancia in distancias.items():
    print(f"Até {no}: {distancia}")