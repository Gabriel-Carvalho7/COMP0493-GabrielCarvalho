
def inversoModular(a, m):
    def euclidesEstendido(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x1, y1 = euclidesEstendido(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
            return gcd, x, y

    gcd, x, _ = euclidesEstendido(a, m)
    if gcd != 1:
        raise Exception("O inverso modular não existe, pois {} e {} não são coprimos.".format(a, m))
    else:
        return x % m

if __name__ == '__main__':
    a = 2
    m = 15
    try:
        inv = inversoModular(a, m)
        print("O inverso modular de {} módulo {} é: {}".format(a, m, inv))
        print("Verificação: ({} * {}) % {} = {}".format(a, inv, m, (a * inv) % m))
    except Exception as e:
        print(e)
