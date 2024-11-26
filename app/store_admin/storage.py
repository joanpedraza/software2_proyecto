from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class StaticFilesStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        if 'local' in settings.ENVIROMENT:
            kwargs['location'] = settings.MEDIA_ROOT
        else:
            kwargs['location'] = settings.STATIC_ROOT
        
        super().__init__(*args, **kwargs)