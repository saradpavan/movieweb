from django.db import models

# Create your models here.

class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()
    def _str_(self):
        return f'message from {self.name}'
        