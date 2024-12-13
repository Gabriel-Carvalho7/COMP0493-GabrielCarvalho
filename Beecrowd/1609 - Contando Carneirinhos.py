casos = int(input())

for _ in range(casos):
    carneiros = int(input())
    contagem = input().split()
    contagem = set(map(int, contagem))
    print(len(contagem))

    