def asistente_ia():
    umbral_alto = 80.0
    umbral_minimo = 40.0
    instruccion = input("Instrucción recibida: ")
    confianza = float(input("Nivel de confianza calculado (0 a 100%): "))

    if confianza < 0 or confianza > 100:
        print("El valor debe estar entre 0 y 100")
        return

    if confianza >= umbral_alto:
        print("Ejecutando la acción: ", instruccion, "... (Éxito)")
        if confianza > 95.0:
            print("Aviso: El modelo ha sido reforzado con éxito debido a la alta precisión.")

    elif umbral_minimo <= confianza < umbral_alto:
        print("Confianza insuficiente. ¿Se refiere a:", instruccion,"? Por favor confirme.")

    else:
        print("Error 404: No pude entender la instrucción. Intente hablar más claro.")

    print("Sesión de procesamiento finalizada.")

def main():
    asistente_ia()

if __name__ == "__main__":
    main()