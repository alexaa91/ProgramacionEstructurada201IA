def acceso_biometrico():
    nombre = input("\nNombre del ingeniero: ")
    id_empleado = int(input("\nID de Empleado: "))
    escaneo_iris = input("\n¿El escaneo de Iris coincide? (si/no): ").lower()
    reconocimiento_facial = input("\n¿El reconocimiento facial es > 95%? (si/no): ").lower()
    if id_empleado <= 0:
         print("\n > Diagnóstico: ¡ALERTA DE SEGURIDAD! ID inválido detectado. Bloqueando accesos y notificando a la policía.")

    elif escaneo_iris == "si" and reconocimiento_facial == "si":
        if id_empleado < 100:
            print(f"\n > Diagnóstico: Bienvenido, Ingeniero {nombre}. Acceso nivel SENIOR concedido a todas las áreas.")
            
        else:
            print(f"\n > Diagnóstico: Bienvenido, Ingeniero {nombre}. Acceso nivel JUNIOR concedido. Áreas de servidores restringidas.")
        
        print(f"\nGenerando log de entrada para el usuario: {id_empleado}...")

    else:
        print("\n > Diagnóstico: Error Biométrico: Identidad no verificada al 100%. Por favor, contacte a seguridad.")

def main():
    print("--- SISTEMA DE CONTROL BIOMÉTRICO ---")
    acceso_biometrico() 

if __name__ == "__main__":
    main()