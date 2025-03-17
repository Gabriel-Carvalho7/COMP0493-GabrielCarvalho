import math

def criaPonto(x, y):
    return (x, y)

def distanciaPonto(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def criaRetaComPontos(p1, p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p2[0] * p1[1] - p1[0] * p2[1]
    return (a, b, c)

def distanciaPontoReta(p, reta):
    a, b, c = reta
    return abs(a * p[0] + b * p[1] + c) / math.sqrt(a**2 + b**2)

def areaPoligono(pontos):
    n = len(pontos)
    if n < 3:
        return 0.0
    
    if pontos[0] != pontos[-1]:
        pontos = pontos + [pontos[0]]
    
    area = 0.0
    for i in range(n):
        x_i, y_i = pontos[i][0], pontos[i][1]
        x_j, y_j = pontos[i+1][0], pontos[i+1][1]
        area += (x_i * y_j) - (x_j * y_i)
    
    return abs(area) / 2.0

def pontoDentroPoligono(p, poligono):
    x, y = p
    dentro = False
    n = len(poligono)
    
    for i in range(n):
        p1 = poligono[i]
        p2 = poligono[(i + 1) % n]
        
        y1, y2 = p1[1], p2[1]
        x1, x2 = p1[0], p2[0]
        
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            dentro = not dentro
    
    return dentro

if __name__ == "__main__":
    A = criaPonto(0, 0)
    B = criaPonto(4, 0)
    C = criaPonto(4, 3)
    D = criaPonto(0, 3)
    E = criaPonto(2, 2)

    print(f"Distância AB: {distanciaPonto(A, B):.2f}")  
    print(f"Reta AC: {criaRetaComPontos(A, C)}") 
    print(f"Distância de E à reta AC: {distanciaPontoReta(E, criaRetaComPontos(A, C)):.2f}") 
    print(f"Área do retângulo: {areaPoligono([A, B, C, D])}") 
    print(f"Ponto E dentro do retângulo? {pontoDentroPoligono(E, [A, B, C, D])}")  