def tabla_multiplicar(n):
    # Encabezado
    print("     ", end="")
    for i in range(1, n+1):
        print(f"{i:4}", end="")
    print()
    
    print("    " + "----" * n)  
    
    # Filas de la tabla
    for fila in range(1, n+1):
        print(f"{fila:2} *", end="")  
        for col in range(1, n+1):
            print(f"{fila*col:4}", end="")
        print()  


def main():
    limite = int(input("¿Hasta qué número vas a multiplicar? "))
    tabla_multiplicar(limite)


if __name__ == "__main__":
    main()