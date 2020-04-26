from django.db import models
from people.models import Gender


class Category(models.Model):
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    name_admin = models.CharField(max_length=100)
    name_to_show = models.CharField(max_length=100)
    image_to_show = models.ImageField(upload_to='categories/')
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name_admin
