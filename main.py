from pulp import LpMaximize, LpProblem, LpVariable, value
import pandas as pd
from optimizador.OptimizationModel import OptimizationModel
from optimizador.Data_loader import Dataloader

"""
    Script de prueba para la lectura y optimización de un problema de maximización de ingresos.
    
"""

if __name__ == "__main__":
    data_loader = Dataloader("data/optimization_problem_data.csv") 
    df = data_loader.load_data()
    model = OptimizationModel(df)
    results = model.optimize()
    for i, result in enumerate(results):
        print(f"Resultado {i}: Estado: {result['Estado']}, x_A: {result['x_A']}, x_B: {result['x_B']}, Ingresos Totales: {result['Ingresos Totales']} \n")
