from django.db import models

# Create your models here.

class Image(models.Model):
    label = models.CharField(max_length=250)
    url = models.URLField()

    def __str__(self):
        return self.label

