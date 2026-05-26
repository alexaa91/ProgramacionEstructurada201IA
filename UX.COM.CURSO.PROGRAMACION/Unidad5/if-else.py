def integer(n):
    if n % 2 == 1:
        print("Weird")
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")

def main():
    n = int(input("Introduce un número entero: "))
    integer(n)

if __name__ == "__main__":
    main()