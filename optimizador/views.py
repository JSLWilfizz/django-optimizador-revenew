# optimizador/views.py
from django.shortcuts import render
from .forms import CSVUploadForm
from .Data_loader import Dataloader
from .OptimizationModel import OptimizationModel
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
                return render(request, 'index.html', {
                    'form': form,
                    'error': 'El archivo debe ser un CSV.'
                })
            # Guardar archivo temporalmente
            with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
                for chunk in archivo.chunks():
                    tmp.write(chunk)
                tmp_path = tmp.name

            try:
                loader = Dataloader(tmp_path)
                parametros = loader.load_data()
                opt_model = OptimizationModel(parametros)
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
