import unittest
import pandas as pd
from optimizador.optimizationModel import OptimizationModel

class TestOptimizationModel(unittest.TestCase):
    def setUp(self):
        # Datos de prueba válidos
            self.df = pd.DataFrame([{
            "Price_Product_A": 50,
            "Price_Product_B": 40,
            "Product_A_Production_Time_Machine_1": 2,
            "Product_B_Production_Time_Machine_1": 1,
            "Product_A_Production_Time_Machine_2": 1,
            "Product_B_Production_Time_Machine_2": 2,
            "Machine_1_Available_Hours": 100,
            "Machine_2_Available_Hours": 80
        }])
            # Valores sacados de la optimización utilizando el script "calculadora_optimizer.py"
            self.resultados_calculadora = {
                "Producto A": 40,
                "Producto B": 20,
                "Ingreso Total": 2800
            }

    def test_output_resultado_optimizacion(self):
        """
         Prueba la estructura de los resultados de la optimización.
         Verifica que se devuelvan las claves esperadas y que los valores no sean None.
        """
        print(self.df)
        model = OptimizationModel(self.df)
        resultados_list = model.optimize()

        for resultados in resultados_list:

            # Verifica que se devuelvan claves esperadas
            self.assertIn("Producto A", resultados)
            self.assertIn("Producto B", resultados)
            self.assertIn("Ingreso Total", resultados)

            print("Resultados de la optimización:", resultados)

            # Verifica que los valores no sean None
            self.assertIsNotNone(resultados["Producto A"])
            self.assertIsNotNone(resultados["Producto B"])
            self.assertIsNotNone(resultados["Ingreso Total"])

            # Verifica que la solución respete las restricciones
            uso_m1 = (
                self.df.at[0, "Product_A_Production_Time_Machine_1"] * resultados["Producto A"] +
                self.df.at[0, "Product_B_Production_Time_Machine_1"] * resultados["Producto B"]
            )
            uso_m2 = (
                self.df.at[0, "Product_A_Production_Time_Machine_2"] * resultados["Producto A"] +
                self.df.at[0, "Product_B_Production_Time_Machine_2"] * resultados["Producto B"]
            )
            self.assertLessEqual(uso_m1, self.df.at[0, "Machine_1_Available_Hours"])
            self.assertLessEqual(uso_m2, self.df.at[0, "Machine_2_Available_Hours"])

    def test_valores_resultados(self):
        """
        Prueba que los valores de los resultados sean correctos.
        Verifica que los ingresos totales se calculen correctamente.
        """


        model = OptimizationModel(self.df)
        resultados_list = model.optimize()

        for resultados in resultados_list:
            ingreso_total_esperado = (
                self.df.at[0, "Price_Product_A"] * resultados["Producto A"] +
                self.df.at[0, "Price_Product_B"] * resultados["Producto B"]
            )
            self.assertEqual(self.resultados_calculadora["Ingreso Total"], ingreso_total_esperado)

            

if __name__ == '__main__':
    unittest.main()
