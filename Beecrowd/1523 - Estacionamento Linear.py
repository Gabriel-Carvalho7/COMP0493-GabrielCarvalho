def main():
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0:
            break

        estacionamento = []
        flag = True

        for _ in range(n):
            c, s = map(int, input().split())

            while estacionamento and estacionamento[-1] <= c:
                estacionamento.pop()

            if len(estacionamento) >= k:
                flag = False
            else:
                if not estacionamento:
                    estacionamento.append(s)
                else:
                    if estacionamento[-1] > s:
                        estacionamento.append(s)
                    else:
                        flag = False

        if not flag:
            print("Nao")
        else:
            print("Sim")

if __name__ == "__main__":
    main()
