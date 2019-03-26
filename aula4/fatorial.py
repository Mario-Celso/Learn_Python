def fatorial (n):

    if n == 0:
        return 1

    else:
        return (n * fatorial(n-1))

if __name__ == "__main__":
    valor = int(input("Informe o valor:"))

    print("Fatorial de %d: %d" %(valor, fatorial(valor)))
