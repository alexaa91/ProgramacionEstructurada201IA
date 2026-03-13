def calificaciones():
    calificacion = float (input("Ingresa la calificación\n"))
    if calificacion >= 90:
        print("Calificación: 'A'")
    elif calificacion >= 80:
        print("Calificación: 'B'")
    elif calificacion >= 70:
        print("Calificación: 'C'")
    elif calificacion >= 69:
        print("Calificación: 'D'")
    else:
        print("Calificación: 'F'")

def main():
    calificaciones()

if __name__ == "__main__":
    main()