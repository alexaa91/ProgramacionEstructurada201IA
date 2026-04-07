"""
    Acumulacion Generica
"""

def Acumulacion():
    suma = 0
    while suma < 500:
        numero = int(input("Ingrese un numero: "))
        suma += numero

    return suma

def main():
    resultado = Acumulacion()
    print("La suma acumulada es: ", resultado)

if __name__ == "__main__":
    main()