from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from django.dispatch import receiver
import shutil
import os
from django.db.models.signals import post_save

from app.store_admin.storage import StaticFilesStorage # type: ignore

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='COP')
    quantity = models.IntegerField()
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True, storage=StaticFilesStorage())

    def __str__(self):
        return self.name

@receiver(post_save, sender=Product)
def copy_image_to_static(sender, instance, created, **kwargs):
    if instance.image:
        image_path = instance.image.path

        if os.path.exists(image_path):
            try:
                volume_path = '/var/lib/containers/railwayapp/bind-mounts/c4830ce2-7cb4-43d3-940c-cc5d4aa3de7a/vol_zumrjcntno8z55j3/product_images'
                #volume_path = '/home/diegomez21/invencloud/'
                dest_path = os.path.join(volume_path, os.path.basename(image_path))
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy(image_path, dest_path)

                print(f"Imagen copiada de {image_path} a {dest_path}")

            except Exception as e:
                print(f"Error al copiar la imagen: {e}")
                
class Provider(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    def __str__(self):
        return self.user.first_name