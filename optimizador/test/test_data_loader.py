import unittest

import pandas as pd
from optimizador.data_loader import Dataloader


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        """
        Establece las columnas esperadas para el DataFrame.
        """
        self.columnas_esperadas = [
            "Price_Product_A",
            "Price_Product_B",
            "Product_A_Production_Time_Machine_1",
            "Product_B_Production_Time_Machine_1",
            "Product_A_Production_Time_Machine_2",
            "Product_B_Production_Time_Machine_2",
            "Machine_1_Available_Hours",
            "Machine_2_Available_Hours"
        ]

    def test_load_data(self):
        """
        Revisa la clase de Dataloader y verifica que el DataFrame no esté vacío.

        También verifica que el DataFrame sea una instancia de pd.DataFrame.
        """
        data_loader = Dataloader("data/optimization_problem_data.csv")
        df = data_loader.load_data()
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty)
    

    def test_columnas_correctas(self):
        """
        Verifica que las columnas del DataFrame sean las esperadas.
        """
        data_loader = Dataloader("data/optimization_problem_data.csv")
        df = data_loader.load_data()
        self.assertListEqual(sorted(list(df.columns)), sorted(self.columnas_esperadas))
    

if __name__ == '__main__':
    unittest.main()