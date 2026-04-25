def normalizar_mensaje(texto):
    return texto.lower().strip()

def detectar_intencion(mensaje):
    comandos = ["encender", "activar", "reproducir"]
    soporte = ["ayuda", "error", "fallo"]

    for palabra in comandos:
        if palabra in mensaje:
            return "COMANDO DE ACCIÓN"

    for palabra in soporte:
        if palabra in mensaje:
            return "REPORTE DE SOPORTE"

    return "CONSULTA GENERAL"

def main():
    mensaje_original = input("Ingrese comando de voz: ")
    mensaje_limpio = normalizar_mensaje(mensaje_original)
    categoria = detectar_intencion(mensaje_limpio)
    longitud = len(mensaje_original)

    print(f'Mensaje Normalizado: "{mensaje_limpio}"')
    print(f"Categoría de Intención: {categoria}")
    print(f"Longitud del mensaje: {longitud} caracteres")

if __name__ == "__main__":
    main()