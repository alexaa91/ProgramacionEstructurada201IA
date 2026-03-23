def sincronizacion():
    frecuencia_A = int(input("Ingrese la Frecuencia A en HZ: "))
    frecuencia_B = int(input("Ingrese la Frecuencia B en HZ: "))

    if frecuencia_A % frecuencia_B == 0 or frecuencia_B % frecuencia_A == 0:
        print("Existe una relacion de sincronización de ciclos")
    else:
        print("No existe sincronización de ciclos")

def main():
    sincronizacion()

if __name__ == "__main__":
    main()