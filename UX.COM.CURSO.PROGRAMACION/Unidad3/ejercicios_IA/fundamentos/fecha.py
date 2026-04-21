def fecha():
    d = int(input("Ingrese el día: "))
    m = int(input("Ingrese el mes: "))
    a = int(input("Ingrese el año: "))

    if a <= 0:
        print("Fecha inválida")
        return
    
    if m < 1 or m > 12:
        print("Fecha inválida")
        return
    
    if m in [ 1, 3, 5, 7, 8, 10, 12]:
        dias_mes = 31
    elif m in [4, 6, 9, 11]:
        dias_mes = 30
    else:
        if(a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            dias_mes = 29
        else:
            dias_mes = 28
    if d >= 1 and d <= dias_mes:
        print("Fecha válida")
    else:
        print("Fecha inválida")

def main():
    fecha()

if __name__ == "__main__":
    main()