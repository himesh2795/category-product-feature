from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    parent = models.ForeignKey('self', null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'
