def modulo_sensores():
    """Procesa el vector de proximidad y retorna el promedio."""
    print("--- MÓDULO DE SENSORES (VECTORES) ---")
    sensores_distancia = []
    
    for i in range(5):
        distancia = float(input(f"Ingrese distancia sensor {i + 1}: "))
        sensores_distancia.append(distancia)
    
    promedio = sum(sensores_distancia) / len(sensores_distancia)
    
    print(f"\nPromedio de proximidad: {promedio:.2f}m.")
    if promedio < 2.0:
        print("Aviso: Reduciendo velocidad global")
    else:
        print("Estado: Seguro.")
    return promedio

def capturar_matriz_vision():
    print("\n--- MÓDULO DE VISIÓN (MATRICES) ---")
    print("Llenando matriz de cámara 3x3:")
    matriz = []
    
    for fila in range(3):
        nueva_fila = []
        for col in range(3):
            brillo = int(input(f"Fila {fila}, Col {col} (Brillo 0-255): "))
            
            # Validación de saturación
            if brillo > 255: brillo = 255
            if brillo < 0: brillo = 0
            
            nueva_fila.append(brillo)
        matriz.append(nueva_fila)
    return matriz

def analizar_brillo(matriz):
    print("\nVisualización de la imagen capturada:")
    puntos_brillantes = 0
    
    for fila in matriz:
        print("[ " + "  ".join(f"{pixel:3}" for pixel in fila) + " ]")
        
        for pixel in fila:
            if pixel > 200:
                puntos_brillantes += 1
                
    print("\n--- RESULTADO DE ANÁLISIS IA ---")
    print(f"Se detectaron {puntos_brillantes} píxeles de alta intensidad.")

def main():
    modulo_sensores()
    
    print("\n" + "="*40)
    
    camara_ia = capturar_matriz_vision()
    
    analizar_brillo(camara_ia)

if __name__ == "__main__":
    main()