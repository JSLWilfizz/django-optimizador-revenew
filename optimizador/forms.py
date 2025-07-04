# optimizador/forms.py
from django import forms

class CSVUploadForm(forms.Form):
    archivo_csv = forms.FileField(label='Sube el archivo CSV de parámetros')