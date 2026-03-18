#Ejemplo de repetición

def ejemplo_for():
    print("Estructura FOR")

    frutas = ["manzana", "banana", "naranja"]

    for fruta in frutas:
        print(fruta)

#for para iterar rangos
    for i in range(1,5):
        print(i)

#for para iterar rangos con pasos
    for i in range(1, 10, 2):
        print(i)

#ejemplo de while
def ejemplo_while():
    print("Estructura WHILE")

    contador = 0

    while contador < 5:
        print(contador)
        contador += 1

#simulacion de Do While
def ejemplo_do_while():
    print("Estructura Do While")

    secreto = "python12"
    intentos = 0

    while True:
        intentos_usuario = "python12" #simulamos la entrada del usuario
        intentos += 1

        if intentos_usuario == secreto:
            print("¡Acceso concedido!")
            break
        else:
            print("¡Acceso denegado! Inténtalo de nuevo.")
            break
        print("\n")

def main():
    ejemplo_for()
    ejemplo_while()
    ejemplo_do_while()

if __name__=="__main__":
     main()  