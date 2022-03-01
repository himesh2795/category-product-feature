from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    price = models.FloatField(null=False)
    category = models.ManyToManyField('modelcore.CategoryModel')

    class Meta:
        db_table = "product"
