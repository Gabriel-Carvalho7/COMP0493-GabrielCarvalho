arr = [0] * 300  

def main():
    c = 1
    bo = False

    while True:
        n = int(input())  
        if n == 0:
            break

        if bo:
            print()
        bo = True

        ta = tp = 0  
        arr = [0] * 300  

        for _ in range(n):
            a, b = map(int, input().split())  
            ta += b
            tp += a
            arr[int(b / a)] += a  

        print(f"Cidade# {c}:")
        c += 1

        j = 0
        for i in range(300):
            if arr[i] > 0:
                if j != 0:
                    print(" ", end="")
                print(f"{arr[i]}-{i}", end="")
                j += 1
        print()


        ip, fp = divmod(int(ta * 100 / tp), 100)  
        if fp < 10:
            print(f"Consumo medio: {ip}.0{fp} m3.")
        else:
            print(f"Consumo medio: {ip}.{fp} m3.")

if __name__ == "__main__":
    main()
