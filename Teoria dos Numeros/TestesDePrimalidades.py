import math

def primalidadeForcaBruta(n):
    if n <= 1:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:  
        return False
 
    max_divisor = math.isqrt(n)
    for i in range(3, max_divisor + 1, 2):  
        if n % i == 0:
            return False
    return True

def primalidadeOtimizado(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    max_divisor = math.isqrt(n)
    i = 5
    while i <= max_divisor:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    numeros = [2, 3, 4, 16, 17, 18, 19, 20, 97, 100]
    
    print("Teste de Primalidade (Força Bruta):")
    for num in numeros:
        print(f"O número {num} é primo? {primalidadeForcaBruta(num)}")
        
    print("\nTeste de Primalidade (Otimizado):")
    for num in numeros:
        print(f"O número {num} é primo? {primalidadeOtimizado(num)}")