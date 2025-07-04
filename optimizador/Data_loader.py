import pandas as pd

class Dataloader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            if not self.file_path.endswith('.csv'):
                raise ValueError("El archivo debe ser un CSV.")
            df = pd.read_csv(self.file_path)
        except Exception as e:
            if not self.file_path.endswith('.csv'):
                raise ValueError("El archivo debe ser un CSV.")
                print(f"Error al cargar el archivo {self.file_path}: {e}")
            else:
                print(f"Error inesperado al cargar el archivo {self.file_path}: {e}")
            return None

        return df
