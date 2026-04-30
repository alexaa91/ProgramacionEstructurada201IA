class ControlAcceso:
    def __init__(self):
        self.usuarios_autorizados = {
            "2024001": "Investigador",
            "2024002": "Estudiante",
            "2024003": "Administrador"
        }

    def verificar_permisos(self, matricula):
        """Valida la matrícula y gestiona los roles."""
        if not matricula.strip():
            raise ValueError("La matrícula no puede estar vacía.")

        if matricula in self.usuarios_autorizados:
            rol = self.usuarios_autorizados[matricula]
            print(f"> [ACCESO CONCEDIDO] Bienvenido, rol detectado: {rol}.")
            
            if rol == "Administrador":
                self.menu_administrador()
        else:
            print("> [ACCESO DENEGADO] Usuario no registrado en la base de datos de IA.")

    def menu_administrador(self):
        """Permite al administrador agregar nuevos usuarios."""
        opcion = input("\n[MODO ADMIN] ¿Desea registrar un nuevo usuario? (s/n): ").lower()
        if opcion == 's':
            nueva_id = input("Ingrese la nueva matrícula: ")
            nuevo_rol = input("Ingrese el rol (Investigador/Estudiante/Administrador): ")
            self.usuarios_autorizados[nueva_id] = nuevo_rol
            print(f"Usuario {nueva_id} registrado exitosamente.")

def main():
    sistema = ControlAcceso()
    print("--- Sistema de Seguridad Laboratorio IA - UX ---")

    while True:
        try:
            matricula_input = input("\nIngrese su matrícula (o 'salir' para finalizar): ")
            
            if matricula_input.lower() == 'salir':
                break
                
            sistema.verificar_permisos(matricula_input)

        except ValueError as e:
            print(f"> [ERROR DE ENTRADA] {e}")
        except Exception as e:
            print(f"> [ERROR INESPERADO] {e}")
        finally:
            print("--- Intento de acceso registrado en el log del servidor ---")

if __name__ == "__main__":
    main()