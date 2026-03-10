#Identificadores validos
nombre_usuario = "Alumno" #inicia con letra y tiene guión bajo
sensor = "Temperatura" #inicia con letra 
_id_interno = 12 #puede contener guion bajo y números

def imprimir_identificadores():
    print(nombre_usuario)
    print(sensor)
    print(_id_interno)

#nombre correcto de funciones
def calcular_area():
    print("Calculando el área...")

def main():
    imprimir_identificadores()
    calcular_area()

if __name__ == "__main__":
    main()