from django.db import models

# Create your models here.


class Manager(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254 , default="@gmail.com")
    phone = models.CharField( max_length=20)
    image = models.ImageField(upload_to="manager/")


    def __str__(self):
        return self.name