from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    category_choices = (
        (0, 'Tapes'),
        (1, 'Glues'),
        (2, 'Grids'),
        (3, 'Gloves'),
    )

    category = models.IntegerField(default=0, choices=category_choices)
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    product_id = models.IntegerField(default=0)
    number = models.IntegerField(default=0)

    def __str__(self):
        return self.name