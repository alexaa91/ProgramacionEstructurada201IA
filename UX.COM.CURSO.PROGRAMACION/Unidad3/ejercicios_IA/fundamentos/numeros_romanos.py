num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def numero_romano():
    n = int(input("Ingresa un número entero positivo menor o igual a 3000: "))
    if n <= 0 or n > 3000:
        print("Error, el número ingresado no cumple las condiciones ")
    else:
        resultado = ""
        i = 0
        while n > 0:
            while n >= num[i]:
                resultado += romanos[i]
                n -= num[i]
            i += 1
        print(f"El número romano es {resultado}")

def main():
    numero_romano()

if __name__ == "__main__":
    main()