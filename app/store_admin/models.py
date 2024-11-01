from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='COP')
    quantity = models.IntegerField()
    provider = models.ForeignKey('Provider', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
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