def division():
    x = int(input("Ingresa el número a dividir: "))
    y = int(input("Ingresa el divisor: "))
    if y == 0:
        print("Error, operación indefinida")
    else:
        cociente = 0
        residuo = x

        while residuo >= y:
            residuo -= y
            cociente += 1
        print(f"El cociente es: {cociente} \nEl residuo es: {residuo}")

def main():
    division()

if __name__ == "__main__":
    main()