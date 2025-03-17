from math import factorial

def coeficiente_binomial_analitico(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def coeficiente_binomial_recursivo(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return coeficiente_binomial_recursivo(n - 1, k - 1) + coeficiente_binomial_recursivo(n - 1, k)

if __name__ == '__main__':
    n = 10
    k = 2
    print("Coeficiente binomial (analítico) de {} sobre {}: {}".format(n, k, coeficiente_binomial_analitico(n, k)))
    print("Coeficiente binomial (recursivo) de {} sobre {}: {}".format(n, k, coeficiente_binomial_recursivo(n, k)))