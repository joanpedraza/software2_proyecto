from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Definir el almacenamiento para imágenes en el directorio staticfiles
class StaticFilesStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs['location'] = str(settings.STATIC_ROOT) + '/product_images'  # Convertir a cadena
        super().__init__(*args, **kwargs)
