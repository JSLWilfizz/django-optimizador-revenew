# optimizador/views.py
from django.shortcuts import render
from .forms import CSVUploadForm
from .data_loader import Dataloader
from .optimizationModel import OptimizationModel
import tempfile

def index(request):
    """
    Vista principal para cargar archivos CSV y mostrar resultados de optimización.
    Esta vista maneja tanto la carga del formulario como la lógica de optimización.
    Si se envía un archivo CSV válido, se procesa y se muestran los resultados de la optimización.
    Si hay un error en el procesamiento del archivo, se muestra un mensaje de error.
    """

    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo_csv']
            if not archivo.name.endswith('.csv'):
                # Condicion anti-error formato: si el archivo no es CSV, mostrar un mensaje de error
                return render(request, 'index.html', {
                    'form': form,
                    'error': 'El archivo debe ser un CSV.'
                })
            # Guardar archivo temporalmente, esto es necesario para que Dataloader pueda leerlo
            # Usamos NamedTemporaryFile para crear un archivo temporal que no se borre al cerrar
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
                for chunk in archivo.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            try:
                loader = Dataloader(tmp_path) # Crear instancia del cargador de datos con la ruta del archivo temporal
                parametros = loader.load_data() # Cargar los datos del archivo CSV usando Dataloader y devuelve un DataFrame de pandas
                opt_model = OptimizationModel(parametros) # Crear instancia del modelo de optimización con los datos cargados
                resultados = opt_model.optimize()
                return render(request, 'resultados.html', {'lista': resultados})

            except Exception as e:
                return render(request, 'index.html', {
                    'form': form,
                    'error': str(e)
                })

    else:
        form = CSVUploadForm()

    return render(request, 'index.html', {'form': form})
