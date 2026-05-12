def telemetria():
    temperatura = float(input("\nTemperatura actual (°C): "))
    porcentaje = int(input("\nUso de Memoria VRAM (%): "))
    enfriamiento = input("\n¿Enfriamiento activo? (si/no): ").lower()

    if porcentaje < 0 or porcentaje > 100:
        print("Error: Lectura de memoria fuera de rango (0-100%).")
        return 
    
    if temperatura > 90 or porcentaje == 100:
        print("¡ALERTA CRÍTICA! Apagando servidores para evitar daños físicos.")
    elif temperatura >= 75:
        if enfriamiento == "no":
            print("\n > Diagnóstico: Peligro: Temperatura alta y enfriamiento desactivado. Pausando entrenamiento.")
        elif enfriamiento == "si":  
            print("\n > Diagnóstico: Temperatura elevada. Reduciendo velocidad de procesamiento (Throttling).")
        else:
            print("\n > Diagnóstico: Entrada inválida para enfriamiento. Por favor, ingrese 'si' o 'no'. ")
    else:
        if porcentaje < 80:
            print("\n > Diagnóstico: Sistema Estable: Entrenamiento en curso a máxima capacidad.")
            memoria_libre = 100 - porcentaje
            print(f"\nMemoria VRAM disponible: {memoria_libre}%")

def main():
    print("--- TELEMETRÍA DE CLUSTER IA ---")
    telemetria()

if __name__ == "__main__":
    main()
        
