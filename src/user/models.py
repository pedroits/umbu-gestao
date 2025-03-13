from django.db import models

from address.models import Address

class User(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=15)
    username = models.CharField(max_length=150)
    institution = models.CharField(max_length=100, null=True)
    education_level = models.IntegerField(null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.SET_NULL)
