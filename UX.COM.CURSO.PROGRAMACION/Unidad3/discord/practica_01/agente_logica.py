""" Funcion que recibe un texto y decide que responder. Implementa Programacacion Estrucutura pura. """

def procesar_pregunta(mensaje_usuario):
    #1.Normalizacion (Paso fundamental en IA)
    mensaje = mensaje_usuario.lower().strip()

    #2.Base de conocimiento (Diccionario)
    conocimiento = {
        #Concepto de Estructura de Control
        "if": "La sentencia 'if' es una condicional. Permite que el programa tome decisiones basandose en una condicion booleana.",
        "for": "Bucle que se usa para recorrer una secuencia (lista, cadena, rango, etc.)",
        "while": "Bucle que repite un bloque de código mientras una condición sea verdadera",
        "break": "Sirve para salir de un bucle antes de que termine",

        #Tipos de Datos
        "int": "Representa un numero entero (ej.5, -10, 0). No tienen parte decimal.",
        "str": "Son textos. Se usan para nombres, mensajes, etc",
        "bool": "Representan valores lógicos: True o False",
        "float": "Números con decimales",

        #Funciones y modularidad
        "def": "Es la palabra reservada para definir una funcion en python",
        "return": "Se usa dentro de una función para devolver un valor como resultado. También finaliza la ejecución de la función en ese punto.",
        "import": "Es la palabra clave que permite usar módulos o funciones definidas en otros archivos dentro de un programa.",
        "from": "Se utiliza junto con import para traer elementos específicos de un módulo, en lugar de importar todo el contenido.",

        #Operadores y Sintaxis
        "print": "Funcion que muestra informacion en la consola o salida estandar",
        "input": "Función que permite recibir datos del usuario desde el teclado. Siempre devuelve el valor como texto (str).",
        "operador_and": "Devuelve True si ambas condiciones son verdaderas.",
        "operador_or": "Devuelve True si al menos una condición es verdadera.",
        "operador_not": "Invierte el valor lógico (True pasa a False y viceversa).",

        #Conceptos de Programacion Estructurada
        "algoritmo": "Es una serie de pasos ordenados y finitos para resolver un problema",
        "programa": "Es un conjunto de instrucciones escritas en un lenguaje de programación que una computadora puede ejecutar para realizar una tarea.",
        "iteracion": "Estructura que permite repetir un bloque de código varias veces mientras se cumpla una condición (por ejemplo, for, while).",
        "variable": "Es un espacio en memoria donde se almacena un dato que puede cambiar durante la ejecución del programa.",

    }

    #3.Logica de busqueda
    for clave in conocimiento:
        if clave in mensaje:
            return conocimiento[clave]

    return "Lo siento, aun no se que es eso. !Preguntame sobre variables, funciones o estructuras de control!"


def main():
    print("Hola! Soy tu asistente de programacion. Preguntame sobre variables, funciones o estructuras de control.")
    
    while True:
        user_input = input("Alumno -> ")
        if user_input.lower() == "salir":
            break

        respuesta = procesar_pregunta(user_input)
        print(f"Bot -> {respuesta}")


# Prueba local (Offline)
if __name__ == "__main__":
    main()