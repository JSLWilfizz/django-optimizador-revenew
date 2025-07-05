
import pandas as pd


"""
Función Hecha por AI para comparar con los resultados de la optimización utilizando la librería pulp.
"""


if __name__ == '__main__':
        # Parámetros del problema
    PA = 50  # Precio producto A
    PB = 40  # Precio producto B

    TA1 = 2  # Tiempo máquina 1 para producto A
    TB1 = 1  # Tiempo máquina 1 para producto B
    TM1 = 100  # Tiempo disponible máquina 1

    TA2 = 1  # Tiempo máquina 2 para producto A
    TB2 = 2  # Tiempo máquina 2 para producto B
    TM2 = 80  # Tiempo disponible máquina 2

    # Variables para guardar la mejor solución
    mejor_xA = 0
    mejor_xB = 0
    max_ingreso = 0

    # Búsqueda por fuerza bruta
    for xA in range(0, 101):       # Ajusta el rango si es necesario
        for xB in range(0, 101):
            tiempo_m1 = TA1 * xA + TB1 * xB
            tiempo_m2 = TA2 * xA + TB2 * xB

            if tiempo_m1 <= TM1 and tiempo_m2 <= TM2:
                ingreso = PA * xA + PB * xB
                if ingreso > max_ingreso:
                    max_ingreso = ingreso
                    mejor_xA = xA
                    mejor_xB = xB

    # Resultado óptimo
    print("Resultados de la optimización:")
    print("Producto A:", mejor_xA)
    print("Producto B:", mejor_xB)
    print("Ingreso Total:", max_ingreso)
