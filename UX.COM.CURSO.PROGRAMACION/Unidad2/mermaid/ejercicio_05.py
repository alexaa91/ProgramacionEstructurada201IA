def suma_condicional():
    suma = 0
    while True:
        numero = int(input("Ingrese un numero: "))
        if numero >= 10 and numero <= 50:
            suma = suma + numero 
        else:
            break
    return suma

def main():
    resultado = suma_condicional()
    print("El resultado es ", resultado)

if __name__ == "__main__":
    main()
