
from django.db import models

# Create your models here.

class moviefront(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='photos')
    video = models.FileField(upload_to='photos')

