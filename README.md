# 🧠 Optimizador de Producción — Revenew

Este proyecto implementa una aplicación Django (solo backend) para cargar un archivo CSV con parámetros de producción y resolver un modelo de optimización lineal. El objetivo es determinar la combinación óptima de productos A y B a fabricar, maximizando los ingresos diarios bajo restricciones de capacidad de dos máquinas.

---

## 📁 Estructura del Proyecto

```bash
revenew_backend/
├── manage.py
├── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── revenew_backend/
│   └── settings.py, urls.py, etc.
├── optimizador/
│   ├── model.py                # Modelo de optimización (PuLP)
│   ├── data_loader.py          # Lector y validador de CSV
│   ├── presenter.py            # Generador de gráficos base64
│   ├── views.py, forms.py, urls.py
│   ├── templates/              # index.html, resultado.html
│   └── tests/                  # Unit tests
