import pandas as pd

class Dataloader:
    def __init__(self, file_path):
        self.file_path = file_path

    
    def check_columnstype(self, df):
        """
        Verifica que las columnas del DataFrame tengan los tipos de datos correctos.
        Realmente podriamos indicar especificamente los tipos de datos esperados como Integers pero para más comodidad y flexibilidad
        me decidi de usar float por si existe algun caso decimal en los datos.

        """

        expected_types = {
            "Price_Product_A": float,
            "Price_Product_B": float,
            "Product_A_Production_Time_Machine_1": float,
            "Product_B_Production_Time_Machine_1": float,
            "Product_A_Production_Time_Machine_2": float,
            "Product_B_Production_Time_Machine_2": float,
            "Machine_1_Available_Hours": float,
            "Machine_2_Available_Hours": float
        }
        for column, expected_type in expected_types.items():
            if column in df.columns and not pd.api.types.is_dtype_equal(df[column].dtype, pd.Series(dtype=expected_type).dtype):
                try:
                    df[column] = pd.to_numeric(df[column], errors='raise') # Agrege esta función para no dar un error si la lectura del type de la columna falla
                except ValueError:
                    raise ValueError(f"La columna '{column}' debe ser de tipo {expected_type.__name__}.") #Ya si no se puede convertir, se lanza un error
        return True

    def load_data(self):
        """
        Carga los datos desde un archivo CSV y realiza las verificaciones necesarias para comprobar si el archivo es un CSV valido.
        """

        try:
            if not self.file_path.endswith('.csv'):
                raise ValueError("El archivo debe ser un CSV.")
            df = pd.read_csv(self.file_path)
            self.check_columnstype(df)
        except Exception as e:
            if not self.file_path.endswith('.csv'):
                raise ValueError("El archivo debe ser un CSV.")
            else:
                raise ValueError(f"Error inesperado al cargar el archivo {self.file_path}: {e}")

        return df
