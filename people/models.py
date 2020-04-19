from django.db import models


class Gender(models.Model):
    name_to_show = models.CharField(max_length=100)
    image_to_show = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name_to_show
