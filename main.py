from optimizador.optimizationModel import OptimizationModel
from optimizador.data_loader import Dataloader

"""
    Script de prueba para la lectura y optimización de un problema de maximización de ingresos.

"""

if __name__ == "__main__":
    try:
        data_loader = Dataloader("data/optimization_problem_data.csv") # Cargar datos desde un archivo CSV
        df = data_loader.load_data()
        model = OptimizationModel(df) # Leer comentarios del archivo optimizador/optimizationModel.py
        results = model.optimize()
        for i, result in enumerate(results):
            print(f"Resultado {i}: Estado: {result['Estado']}, Producto A: {result['Producto A']}, Producto B: {result['Producto B']}, Ingreso Total: {result['Ingreso Total']} \n")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        # Aquí se podria manejar el error de forma más específica, pero ya es redundante