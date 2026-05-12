def patronmaestro():
    patron_maestro = [1, 0, 1, 1, 0]
    lectura_sensor = []

    print("--- ESCÁNER BIOMÉTRICO DE IA ---")

    for i in range(5):
        bit = int(input(f"Ingrese bit {i + 1} (0 o 1): "))
        lectura_sensor.append(bit)

    print("\n> Comparando lectura con base de datos...")

    coincidencias = 0

    for i in range(5):
        if lectura_sensor[i] == patron_maestro[i]:
            coincidencias += 1

    similitud = (coincidencias / 5) * 100

    print(f"\n> Coincidencias encontradas: {coincidencias}")
    print(f"> Porcentaje de Similitud: {similitud}%")

    if similitud == 100:
        print("\nACCESO TOTAL: Identidad Verificada.")
    elif similitud >= 60:
        print("\nADVERTENCIA: Similitud parcial. Se requiere verificación manual.")
    else:
        print("\nALERTA: Intruso detectado. Sistema bloqueado.")

    print("\nComparación de listas")
    print("Patrón Maestro :", patron_maestro)
    print("Lectura Sensor :", lectura_sensor)


def main():
    patronmaestro()


if __name__ == "__main__":
    main()