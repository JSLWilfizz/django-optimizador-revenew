import pulp
from .data_loader import Dataloader
import pandas as pd

class OptimizationModel:
    def __init__(self, data = None):
        """
        Inicializa el modelo de optimización con los datos proporcionados.
        
        :param data: DataFrame de pandas que contiene los parámetros del problema de optimización."""
        if data is None:
            raise ValueError("Los datos de entrada no pueden ser None. Por favor, proporciona un DataFrame de pandas.")
        self.data = data

    def optimize(self):
        """# Crear el problema de optimización
        # Asumimos que 'data' es un DataFrame de pandas con las columnas necesarias
        # y que contiene las siguientes columnas:
        # - Price_Product_A
        # - Price_Product_B
        # - Product_A_Production_Time_Machine_1
        # - Product_B_Production_Time_Machine_1
        # - Product_A_Production_Time_Machine_2
        # - Product_B_Production_Time_Machine_2
        # - Machine_1_Available_Hours
        # - Machine_2_Available_Hours 
        # El objetivo es maximizar los ingresos totales de la producción de dos productos
        # A y B, dados los precios y tiempos de producción en dos máquinas.
        # El resultado será un DataFrame con los resultados de la optimización para cada fila del DataFrame original.
        # El resultado incluirá el estado de la solución, las cantidades óptimas de los productos A y B
        # y los ingresos totales generados.

        #Comentarios Javier:
            Realmente esto podría hacerse de una forma de que el usuario final seleccione las columnas y defina cada parámetro de la optimización.
        # Por ejemplo, el usuario podría seleccionar el nombre de las columnas que contienen los precios de los productos, los tiempos
        # de producción y las horas disponibles de las máquinas. Esto permitiría una mayor flexibilidad y adaptabilidad del
        # modelo a diferentes conjuntos de datos, pero requiere una interfaz de usuario más compleja.
        # 
        # 
        # Return Lista de diccionarios
        # 
        # """
        results = []
        for index, row in self.data.iterrows():
            self.Price_Product_A = row["Price_Product_A"]
            self.Price_Product_B = row["Price_Product_B"]
            self.Product_A_Production_Time_Machine_1 = row["Product_A_Production_Time_Machine_1"]
            self.Product_B_Production_Time_Machine_1 = row["Product_B_Production_Time_Machine_1"]
            self.Product_A_Production_Time_Machine_2 = row["Product_A_Production_Time_Machine_2"]
            self.Product_B_Production_Time_Machine_2 = row["Product_B_Production_Time_Machine_2"]
            self.Machine_1_Available_Hours = row["Machine_1_Available_Hours"]
            self.Machine_2_Available_Hours = row["Machine_2_Available_Hours"]

            model = pulp.LpProblem(name="maximizar-ingresos", sense=pulp.LpMaximize)

            # Variables de decisión (>= 0)
            x_A = pulp.LpVariable(name="x_A", lowBound=0, cat='Integer')
            x_B = pulp.LpVariable(name="x_B", lowBound=0, cat='Integer')

            # Función objetivo
            model += self.Price_Product_A * x_A + self.Price_Product_B * x_B, "IngresosTotales"

            # Restricciones
            model += self.Product_A_Production_Time_Machine_1 * x_A + self.Product_B_Production_Time_Machine_1 * x_B <= self.Machine_1_Available_Hours, "Restriccion_Maquina_1"
            model += self.Product_A_Production_Time_Machine_2 * x_A + self.Product_B_Production_Time_Machine_2 * x_B <= self.Machine_2_Available_Hours, "Restriccion_Maquina_2"

            # Resolver
            model.solve()
            # Mostrar resultados
            result = {
                "Estado": pulp.LpStatus[model.status],
                "Producto A": x_A.varValue,
                "Producto B": x_B.varValue,
                "Ingreso Total": pulp.value(model.objective)
            }

            results.append(result)

        return results