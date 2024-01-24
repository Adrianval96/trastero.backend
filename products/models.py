from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.FloatField()

    class Meta:
        db_table = "products"
