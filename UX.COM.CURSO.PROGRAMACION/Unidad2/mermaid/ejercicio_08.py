def acceso():
    intentos = 0
    clave_correcta = '1234'
    while intentos < 3:
        contraseña = input("Ingrese clave: ")

        if contraseña == clave_correcta:
            print("Acceso concecido")
            return

        else:
            intentos += 1
            print("Contraseña incorrecta")

    print("Cuenta bloqueada")

def main():
    acceso()

if __name__ == "__main__":
    main()
