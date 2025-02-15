def binaryExponentiation(base, exponent):
    if exponent < 0:
        print("\nErro\n")
        return
    
    resultado = 1
    
    while exponent > 0:
        if exponent % 2 == 1:
            resultado *= base
        base *= base
        exponent //= 2
    
    return resultado

if __name__ == "__main__":
    print(f"\nBinaryExponentiation: {binaryExponentiation(2, 13)}\n") 
