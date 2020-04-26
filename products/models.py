from django.db import models
from categories.models import Category


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_to_show = models.CharField(max_length=100)
    image_to_show = models.ImageField(upload_to='products/')
    image_to_show_two = models.ImageField(upload_to='products/')
    available = models.BooleanField(default=True)
    sizes_s = models.IntegerField(default=0)
    sizes_m = models.IntegerField(default=0)
    sizes_l = models.IntegerField(default=0)
    sizes_xl = models.IntegerField(default=0)
    sizes_xxl = models.IntegerField(default=0)
    description = models.TextField()
    price = models.FloatField(default=0)
