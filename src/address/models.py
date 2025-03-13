from django.db import models

class Address(models.Model):
    street_name = models.CharField(max_length=150)
    neighborhood = models.CharField(max_length=150)
    city_name = models.CharField(max_length=150)
    house_number = models.CharField(max_length=10)
    street_zipcode = models.CharField(max_length=20, null=True)
    complement = models.CharField(max_length=150, null=True)
