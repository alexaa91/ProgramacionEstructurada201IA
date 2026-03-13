#Implementación de Match en Python
def demostracion():
    print("-- Ejemplos de match --")
    opcion = input("Ingrese una opción (1-3):")

    match opcion:
        case "1":
            print("Opción 1 es seleccionada")
            nombre = input("Ingrese su nombre: ")
            print(f"Hola, {nombre}!")
        case "2":
            print("Opción 2 es seleccionada")
            matricula = input("Ingrese su matrícula: ")
            print(f"Su matrícula es: {matricula}")
        case "3":
            print("Opción 3 es seleccionada")
            semestre = input("Ingrese su semestre: ")
            print(f"Usted está en el semestre: {semestre}")
        case _:
            print("Opción no válida")

def main():
    demostracion()

if __name__ == "__main__":
    main()