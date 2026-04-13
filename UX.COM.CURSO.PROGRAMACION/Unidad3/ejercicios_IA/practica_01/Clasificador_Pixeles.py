#limpieza de datos, normalizacion
UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificador_pixeles():
    intensidad = float(input("Ingrese la intensidad del pixel (0.0 a 0.1): "))
    
    if intensidad < 0.0 or intensidad > 1.0:
        print("Error: Valor de pixel inválido")
        return
    
    if 0.0 <= intensidad <= UMBRAL_BAJO:
        print("Clasificación (Fondo Oscuro)")
        return
    
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        print("Clasificacion (Fondo Gris)")
        return
    
    if intensidad >= UMBRAL_ALTO:
        print("Clasificacion (Objeto Brillante)")
        return
    
    print("Análisis de imagen finalizado")

def main():
    clasificador_pixeles()

if __name__ == "__main__":
    main()
