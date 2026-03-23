def entrenamiento():
    memoria = 0
    while memoria <= 2500:
        lote = float(input("Ingrese el tamaño del lote en MB: "))
        if lote > 0:
            memoria += lote
            print("La memoria actual es de ", memoria, "MB")
        else:
            print("Ingresa un valor válido")
            
    print("La memoria VRAM alcanzó su limite")
    print("El valor final de la memoria fue de ", memoria, "MB")

def main():
    entrenamiento()

if __name__ == "__main__":
    main()
