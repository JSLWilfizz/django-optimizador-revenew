import unittest
import pandas as pd
from optimizador.model import OptimizationModel

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

    def test_resultado_optimizacion(self):
        model = OptimizationModel(self.df)
        resultados = model.optimize()

        # Verifica que se devuelvan claves esperadas
        self.assertIn("x_A", resultados)
        self.assertIn("x_B", resultados)
        self.assertIn("Ingreso total", resultados)

        # Verifica que los valores no sean None
        self.assertIsNotNone(resultados["x_A"])
        self.assertIsNotNone(resultados["x_B"])
        self.assertIsNotNone(resultados["Ingreso total"])

        # Verifica que la solución respete las restricciones
        uso_m1 = (
            self.df.at[0, "Product_A_Production_Time_Machine_1"] * resultados["x_A"] +
            self.df.at[0, "Product_B_Production_Time_Machine_1"] * resultados["x_B"]
        )
        uso_m2 = (
            self.df.at[0, "Product_A_Production_Time_Machine_2"] * resultados["x_A"] +
            self.df.at[0, "Product_B_Production_Time_Machine_2"] * resultados["x_B"]
        )
        self.assertLessEqual(uso_m1, self.df.at[0, "Machine_1_Available_Hours"])
        self.assertLessEqual(uso_m2, self.df.at[0, "Machine_2_Available_Hours"])

if __name__ == '__main__':
    unittest.main()