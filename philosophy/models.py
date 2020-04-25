from django.db import models


class Philosophy(models.Model):
    speech = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
