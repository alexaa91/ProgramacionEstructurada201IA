peliculas_accion = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror = ["It", "The Conjuring", "Saw"]

def obtener_recomendacion():
    edad_usuario = int(input("Ingresa tu edad: "))
    genero_elegido = input("¿Qué género prefiere (accion/comedia/terror)?: ").lower()
    
    if edad_usuario < 13:
        if genero_elegido == "terror":
            print("Nota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")
        return peliculas_comedia[0]
    
    if genero_elegido == "accion":
        return peliculas_accion[0]
    elif genero_elegido == "terror":
        return peliculas_terror[0]
    elif genero_elegido == "comedia":
        return peliculas_comedia[0]
    else:
        print("Género no válido")

def main():
    recomendacion = obtener_recomendacion()
    print("Recomendación de la IA: ", recomendacion)

if __name__ == "__main__":
    main()

