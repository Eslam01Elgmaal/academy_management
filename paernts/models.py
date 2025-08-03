from django.db import models

# Create your models here.

class Paernt(models.Model):
    name = models.CharField(max_length=80)
    addres = models.CharField(max_length=180)




    def __str__(self):
        return self.name
    