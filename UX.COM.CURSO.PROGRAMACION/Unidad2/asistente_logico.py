from datetime import datetime
def asistente():
    nombre_asistente = "IA-UX"
    print("Bienvenida, soy tu asistente ", nombre_asistente)
    comando = input("¿En qué puedo ayudarte hoy? ").lower()

    if "hola" in comando or "buenos dias" in comando:
        print("¡Hola! Soy tu asistente. Es un gusto saludarte.")

    elif "clima" in comando or "temperatura" in comando:
        print("Consultando el servicio meteorológico... Hoy en Xalapa tendremos un día nublado.")
    
    elif "hora" in comando or "tiempo" in comando:
        hora_actual = datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual del sistema es: ", hora_actual)

    else:
        print("Lo siento, todavía no entiendo ese comando. ¿Podrías intentar con otra palabra?")
    
    print("Proceso finalizado. Gracias por usar ", nombre_asistente)
    
def main():
    asistente()

if __name__ == "__main__":
    main()