def dias():
    opcion = input("Ingrese una opción (1-7):")

    match opcion:
        case "1":
            print("Día Lunes")
        case "2":
            print("Día Martes")
        case "3":
            print("Día Miércoles")
        case "4":
            print("Día Jueves")
        case "5":
            print("Día Viernes")
        case "6":
            print("Día Sábado")
        case "7":
            print("Día Domingo")
        case _:
            print("Número inválido")

def main():
    dias()

if __name__ == "__main__":
    main()