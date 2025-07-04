# Optimizador de Producción – Prueba Técnica (Revenew)

Este proyecto implementa una aplicación backend en Django que permite:

✅ Subir un archivo CSV con parámetros de producción  
✅ Ejecutar un modelo de optimización lineal entera  
✅ Obtener la combinación óptima de productos A y B que maximiza los ingresos diarios  
✅ Visualizar los resultados en formato tabla y gráfico  
✅ (Opcional) Ejecutar desde un `main.py` sin necesidad de servidor web  
✅ (Opcional) Desplegar fácilmente con Docker

---

## 🧠 Descripción del modelo

El modelo de optimización busca **maximizar el ingreso total**, sujeto a restricciones de capacidad de dos máquinas.  
Las variables de decisión (x_A, x_B) representan la cantidad a producir de los productos A y B, y están definidas como **enteras**.

Función objetivo:

```
Max Z = P_A * x_A + P_B * x_B
```

Restricciones:

```
T_A1 * x_A + T_B1 * x_B ≤ TM_1
T_A2 * x_A + T_B2 * x_B ≤ TM_2
x_A, x_B ≥ 0 (enteros)
```

---

## 📁 Estructura del proyecto

```
.
├── main.py                      # Ejecuta el optimizador desde consola
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── revenew_backend/            # Proyecto Django
│   └── settings.py, urls.py...
├── optimizador/                # App principal
│   ├── data_loader.py          # Clase para cargar y validar el CSV
│   ├── optimizationModel.py     # Clase OptimizationModel con PuLP
│   ├── presenter.py            # Genera gráficos (matplotlib)
│   ├── views.py, forms.py, urls.py
│   ├── templates/
│   │   └── optimizador/
│   │       ├── index.html      # Formulario de carga
│   │       └── resultado.html  # Resultados optimizados + gráfico
│   └── tests/                  # Pruebas unitarias
```

---

## 🚀 Cómo ejecutar

### 🔧 Requisitos

- Python 3.10
- pip
- Docker (opcional)

---

### ▶️ Opción 1: Entorno local

1. Crear entorno virtual

```bash
python3.10 -m venv venv
source venv/bin/activate  # o .\venv\Scripts\Activate.ps1 en Windows
```

2. Instalar dependencias

```bash
pip install -r requirements.txt
```

3. Ejecutar Django

```bash
python manage.py runserver
```

4. Abrir en el navegador:  
[http://localhost:8000](http://localhost:8000)

---

### 🐳 Opción 2: Docker

1. Build y ejecución rápida:

```bash
docker-compose up --build
```

2. Abrir en el navegador:  
[http://localhost:8000](http://localhost:8000)

---
---

## 📊 Ejecución directa con `main.py`

Para probar el optimizador sin levantar el servidor web:

1. Asegúrate de tener un archivo `$NOMBRE_ARCHIVO.csv` con estructura como:

```csv
Price_Product_A,Price_Product_B,Product_A_Production_Time_Machine_1,Product_B_Production_Time_Machine_1,Product_A_Production_Time_Machine_2,Product_B_Production_Time_Machine_2,Machine_1_Available_Hours,Machine_2_Available_Hours
50,40,2,1,1,2,100,80
```

2. Ejecuta:

```bash
python main.py
```

---

## 🙋‍♂️ Autor

Javier Soto Letelier

---