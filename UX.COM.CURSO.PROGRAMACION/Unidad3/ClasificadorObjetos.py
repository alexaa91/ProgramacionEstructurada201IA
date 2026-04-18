umbral_pequeno = 5.0
umbral_grande = 20.0

def clasificacion():
    dimension = float(input("Ingrese el tamaño del objeto detectado (cm): "))
    if dimension <= 0.0:
        print("Error: Lectura inválida. Verifique el sensor.")
    elif dimension <= umbral_pequeno:
        print("Clasificación: Micro-componente (Grado A)")
    elif dimension <= umbral_grande:
        print("Clasificación: Componente Estándar (Grado B)")
    else:
        print("Clasificación: Componente Industrial (Grado C)")
    
        volumen = dimension ** 3
        print(f"Espacio requerido en contenedor: {volumen} cm3")

    print("Registro de inspección completado.")

def main():
    clasificacion()

if __name__ == "__main__":
    main()