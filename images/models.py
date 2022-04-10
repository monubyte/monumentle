from django.db import models

# Create your models here.

class Image(models.Model):

    label = models.CharField(max_length=250)
    url = models.URLField()

    # def save(self, *args, **kwargs):
    #     self.l
    #     super(Image, self).save(*args, **kwargs)
    def __str__(self):
        return self.label

    def get_ids(self):
        return self.objects.values_list('id', flat=True)

