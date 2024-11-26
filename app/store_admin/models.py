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
    image = models.ImageField(upload_to='product_images/', null=True, blank=True) #storage=StaticFilesStorage()

    def __str__(self):
        return self.name

@receiver(post_save, sender=Product)
def delete_image_on_update(sender, instance, created, **kwargs):
    if instance.image:
        old_instance = Product.objects.filter(pk=instance.pk).first()
        if old_instance and old_instance.image != instance.image:
            old_image = old_instance.image
            if old_image:
                storage = old_image.storage
                storage.delete(old_image.name)
    else:
        if instance.pk:
            old_instance = Product.objects.get(pk=instance.pk)
            if old_instance.image:
                old_image = old_instance.image
                storage = old_image.storage
                storage.delete(old_image.name)
                
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