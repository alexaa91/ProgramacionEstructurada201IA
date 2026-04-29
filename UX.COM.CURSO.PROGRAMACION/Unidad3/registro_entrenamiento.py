class MonitorEntrenamiento:
    def __init__(self, umbral_convergencia=0.01):
        self.historial_errores = []
        self.umbral_convergencia = umbral_convergencia

    def registrar_epoca(self, valor_error):
        self.historial_errores.append(valor_error)
        
        if valor_error < self.umbral_convergencia:
            print(f"[SISTEMA] Entrenamiento completado: Se alcanzó el objetivo de precisión (Error: {valor_error})")
        else:
            print("> Registro exitoso.")

print("Iniciando Monitor de Red Neuronal")
monitor = MonitorEntrenamiento(umbral_convergencia=0.05) 

epocas_a_registrar = 5
contador = 1

while contador <= epocas_a_registrar:
    try:
        entrada = input(f"\nIngrese el error de la Época {contador}: ")
        valor = float(entrada)

        if valor < 0:
            print("> [ERROR] El error no puede ser un número negativo.")
            continue

        monitor.registrar_epoca(valor)
        contador += 1

    except ValueError:
        print("> [ERROR] Entrada inválida. Por favor, ingrese un número decimal.")


if monitor.historial_errores:
    print("\nResumen de Entrenamiento")
    print(f"Historial: {monitor.historial_errores}")
    
    promedio = sum(monitor.historial_errores) / len(monitor.historial_errores)
    print(f"Promedio de Error: {promedio:.4f}")
    
    mejor_error = min(monitor.historial_errores)
    print(f"Mejor resultado obtenido: {mejor_error}")
else:
    print("No se registraron datos válidos.")