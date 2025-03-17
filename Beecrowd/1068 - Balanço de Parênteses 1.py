while True:
    try:
        permitidos = "()"
        expressao = input()
        abre = "".join(c for c in expressao if c in permitidos[0])
        fecha = "".join(c for c in expressao if c in permitidos[1])
        ambos = "".join(c for c in expressao if c in permitidos)

        if len(abre) != len(fecha):
            print("incorrect")
        else:
            valido = True
            abriu = fechou = 0
            for char in ambos:
                if char == '(':
                    abriu += 1
                else:
                    fechou += 1
                
                if char == permitidos[1] and fechou > abriu:
                    print("incorrect")
                    valido = False
                    break

            if valido:
                print("correct")
    except EOFError:
        break