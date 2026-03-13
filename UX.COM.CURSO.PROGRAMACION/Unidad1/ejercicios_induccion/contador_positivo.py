#Desarrollo de aloritmo Contador de Algoritmos

#Función que cuenta cuántos números positivos ingresa el usuario
def contador_positivos():
    contador = 0
    while True: #Bucle que se ejecuta hasta que el usuario decida terminar
        numero = int(input("Ingrese un numero(-1 para terminar):"))
        if numero < 0 : 
            break
        contador += 1

    print("Cantidad de mnumeros positivos ingresados:", contador)

#Definicion de la funcion (Controla el flujo del programs)
def main():
    print("Bienvenido al contador de numeros positivos")
    contador_positivos() #Llama a la función que cuenta los números

#Llamada a 
if __name__ == "__main__":
    main()