#limpieza de datos, normalizacion
UMBRAL_ALTO = 0.7
UMBRAL_BAJO = 0.3

def clasificador_pixeles(intensidad):
    
    if intensidad < 0.0 or intensidad > 1.0:
        return None
    
    if 0.0 <= intensidad <= UMBRAL_BAJO:
        return "(Fondo Oscuro)"
    
    if UMBRAL_BAJO < intensidad < UMBRAL_ALTO:
        return "Gris(Ruido)"
    
    if intensidad >= UMBRAL_ALTO:
        return "Objeto (Brillante)"
    
    print("Análisis de imagen finalizado")

import os

def cargar_y_procesar(nombre_archivo):
    datos_limpios = []
    ruido_detectado = 0
    fondo_oscuro = 0
    gris_ruido = 0
    objeto_brillante = 0


    ruta_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(ruta_script, nombre_archivo)

    try:
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                #convertir cada linea a numero flotante
                valor_crudo = float(linea.strip())

                #clasificar el valor del pixel
                clasificacion = clasificador_pixeles(valor_crudo)

                #agregamos la logica de clasificacion
                if clasificacion is None:
                    ruido_detectado += 1
                else:
                    datos_limpios.append(clasificacion)
                    if clasificacion == "(Fondo Oscuro)":
                        fondo_oscuro += 1
                    elif clasificacion == "Gris(Ruido)":
                        gris_ruido += 1
                    elif clasificacion == "Objeto (Brillante)":
                        objeto_brillante += 1
        
        print("Resultados de Clasificación: ")
        print(f"Fondo Oscuro: {fondo_oscuro}")
        print(f"Gris (Ruido): {gris_ruido}")
        print(f"Objeto (Brillante): {objeto_brillante}")
        print(f"Ruido Detectado: {ruido_detectado}")
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se encontró")


def main():
    cargar_y_procesar("lecturas_sensores.txt")

if __name__ == "__main__":
    main()
