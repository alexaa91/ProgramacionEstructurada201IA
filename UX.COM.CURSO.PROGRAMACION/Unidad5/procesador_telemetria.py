# ==========================================
# IMPORTACIÓN DE BIBLIOTECAS (Biblioteca Estándar)
# ==========================================
import sys

# ==========================================
# PEGA AQUÍ LAS 3 FUNCIONES GENERADAS POR IA
# ==========================================

def limpiar_lecturas(lista_datos):
    """
    Filtra una lista de lista_datos LIDAR eliminando valores atípicos o inválidos.

    Recorre cada valor de la lista recibida y conserva únicamente aquellos
    que se encuentran dentro del rango válido [0.0, 100.0] metros. Los valores
    fuera de ese rango se consideran errores de lectura del sensor y son
    descartados.

    Parámetros:
        lista_datos (list[float]): Lista de distancias en metros reportadas
                                por el sensor LIDAR del robot.

    Retorna:
        list[float]: Nueva lista que contiene solo los valores válidos,
                     es decir, aquellos donde 0.0 <= valor <= 100.0.
                     Si la lista de entrada está vacía o todos los valores
                     son inválidos, se retorna una lista vacía.

    Ejemplos:
        >>> limpiar_lecturas([1.5, -0.3, 45.0, 101.2, 78.9])
        [1.5, 45.0, 78.9]

        >>> limpiar_lecturas([-5.0, 200.0])
        []

        >>> limpiar_lecturas([0.0, 50.0, 100.0])
        [0.0, 50.0, 100.0]
    """
    lecturas_validas = []

    if lista_datos is None:
        return lecturas_validas

    for lectura in lista_datos:
        if lectura >= 0.0 and lectura <= 100.0:
            lecturas_validas.append(lectura)

    return lecturas_validas


def calcular_alertas(lista_filtrada, umbral_critico):
    """
    Cuenta cuántas lecturas LIDAR están por debajo de un umbral crítico de distancia.

    Recorre la lista de lecturas ya validadas y acumula un contador cada vez
    que una distancia es menor al umbral crítico indicado, lo que representa
    un riesgo de colisión inmediata para el robot.

    Parámetros:
        lista_filtrada (list[float]): Lista de distancias válidas en metros,
                                       previamente filtrada por limpiar_lecturas.
        umbral_critico (float):         Distancia mínima de seguridad en metros.
                                        Cualquier lectura menor a este valor
                                        genera una alerta de colisión.

    Retorna:
        int: Número total de lecturas que se encuentran por debajo del
             umbral crítico. Retorna 0 si la lista está vacía, es None,
             o si el umbral_critico no es un número válido (negativo o None).

    Ejemplos:
    >>> calcular_alertas([1.5, 3.0, 0.8, 12.4, 2.1], 2.5)
        3

    >>> calcular_alertas([10.0, 20.0, 30.0], 5.0)
        0

    >>> calcular_alertas([], 2.5)
        0
    """
    alertas = 0

    if lista_filtrada is None:
        return alertas

    if umbral_critico is None:
        return alertas

    if umbral_critico < 0.0:
        return alertas

    for lectura in lista_filtrada:
        if lectura < umbral_critico:
            alertas += 1

    return alertas

def generar_log_sistema(total_alertas):
    """
    Genera una cadena de texto formateada con el log del sistema LIDAR.

    Utiliza el módulo sys para detectar la plataforma del sistema operativo
    en ejecución e incluye el total de alertas críticas detectadas junto con
    la acción recomendada: PERMITIDA si las alertas son 3 o menos, o ABORTAR
    si superan ese límite, indicando riesgo de colisión inminente.

    Parámetros:
        total_alertas (int): Número de alertas críticas detectadas, generado
                             por la función calcular_alertas. Debe ser un
                             entero mayor o igual a 0.

    Retorna:
        str: Cadena de texto con el log formateado:
             "[SISTEMA <OS>] Alertas críticas encontradas: <X>. Acción: <ACCIÓN>"
             Retorna un mensaje de error descriptivo si el parámetro es
             inválido (None, negativo o no entero).

    Ejemplos:
        >>> generar_log_sistema(2)
        '[SISTEMA linux] Alertas críticas encontradas: 2. Acción: PERMITIDA'

        >>> generar_log_sistema(5)
        '[SISTEMA linux] Alertas críticas encontradas: 5. Acción: ABORTAR'

        >>> generar_log_sistema(-1)
        '[ERROR] total_alertas no puede ser un valor negativo.'
    """
    LIMITE_ABORTAR = 3

    if total_alertas is None:
        return "[ERROR] total_alertas no puede ser None."

    if not isinstance(total_alertas, int):
        return "[ERROR] total_alertas debe ser un número entero."

    if total_alertas < 0:
        return "[ERROR] total_alertas no puede ser un valor negativo."

    plataforma = sys.platform

    if total_alertas > LIMITE_ABORTAR:
        accion = "ABORTAR"
    else:
        accion = "PERMITIDA"

    log = (
        f"[SISTEMA {plataforma}] "
        f"Alertas críticas encontradas: {total_alertas}. "
        f"Acción: {accion}"
    )

    return log


# ==========================================
# PROGRAMA PRINCIPAL (Orquestación Manual)
# ==========================================
if __name__ == "__main__":
    lecturas_raw = [12.5, -5.0, 88.2, 120.1, 1.2, 0.0, 45.6, 2.5]
    UMBRAL = 3.0
   
    print("=== SISTEMA DE TELEMETRÍA DE AGENTE AUTÓNOMO ===\n")
   
    # RETO DEL ALUMNO:
    
    datos_limpios = limpiar_lecturas(lecturas_raw)
    alertas = calcular_alertas(datos_limpios, UMBRAL)
    log_final = generar_log_sistema(alertas)
    print(log_final)

"""
1. Propmt utilizado: 
    "Actúa como un programador experto en Python Estructurado. Escribe el código de una función llamada 
    limpiar_lecturas. Recibe como parámetro una lista de números flotantes que representan distancias a obstáculos detectados
    por el LIDAR del robot y debe retornar una nueva lista filtrada con los valores válidos (eliminando los valores atípicos 
    menores a 0.0 o mayores a 100.0, que se consideran errores de lectura). Restricciones estrictas: 1. No utilices programación 
    orientada a objetos (POO). 2. No utilices manejo de excepciones (nada de bloques try-except). Gestiona los errores de datos usando 
    condicionales if/else tradicionales. 3. Incluye la documentación de la función mediante un Docstring descriptivo."
2. Tabla de Pruebas de Escritorio Manual (Trace Table):
- lecturas_raw = [-15.0, 150.5, -1.0]
- UMBRAL = 5.0

Fase 1: Ejecución de limpiar_lecturas([-15.0, 150.5, -1.0])
  - Inicialización: lista_validos = []
  - Iteración 1: elemento = -15.0. Condición (-15.0 >= 0.0) es False. No se añade
  - Iteración 2: elemento = 150.5. Condición (150.5 <= 100.0) es False. No se añade
  - Iteración 3: elemento = -1.0. Condición (-1.0 >= 0.0) es False. No se añade
  - Fin de ciclo. Retorna: []
  - Variable global asignada: datos_limpios = []

Fase 2: Ejecución de calcular_alertas([], 5.0)
  - Inicialización: total_alertas = 0
  - Ciclo for: Como la lista 'datos_limpios' está vacía, el bucle no realiza ninguna iteración
  - Fin de ciclo. Retorna: 0
  - Variable global asignada: alertas_detectadas = 0

Fase 3: Ejecución de generar_log_sistema(0)
  - Variable 'plataforma' toma el valor de sys.platform (Ej: 'WIN32')
  - Condición evaluada: ¿total_alertas (0) > 3? Es False
  - Variable 'accion' toma el valor: "PERMITIDA"
  - Retorna: "[WIN32] Alertas críticas encontradas: 0. Acción: PERMITIDA"

3. ¿La IA intentó utilizar sintaxis avanzada? No, debido a las restricciones estrictas que fueron especificadas en el propmt, 
la IA se limitó a utilizar estructuras de control básicas como condicionales if/else y ciclos for tradicionales, 
evitando cualquier sintaxis avanzada o características de programación orientada a objetos
"""