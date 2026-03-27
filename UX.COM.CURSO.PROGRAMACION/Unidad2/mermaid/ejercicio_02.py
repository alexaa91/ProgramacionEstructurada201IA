def factorial():
    N = int(input("Ingresa un numero: "))
    factorial = 1
    i = 1
    while i<=N:
        factorial = factorial * i
        i = i+1
    return factorial

def main():
    Nfactorial= factorial()
    print(Nfactorial)

if __name__ == "__main__":
    main()