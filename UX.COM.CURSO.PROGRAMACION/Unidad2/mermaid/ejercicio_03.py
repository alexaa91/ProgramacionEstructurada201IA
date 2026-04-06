def impares():
    N = int(input("Ingrese cantidad de números impares a mostrar: "))
    contador = 0
    numero = 1
    while contador < N:
        print(numero)
        numero = numero + 2
        contador = contador + 1

def main():
    impares()

if __name__ == "__main__":
    main()
