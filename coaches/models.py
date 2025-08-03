from django.db import models
from django.urls import reverse

# Create your models here.


class Coaches(models.Model):
    Coaches_CHOICES = [
        ('TEC', 'Technical director'),
        ('SPO', 'Sports director'),
        ('ASS', 'Assistant coach'),
    ]

    job_title = models.CharField(max_length=3, choices=Coaches_CHOICES)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254 , default="@gmail.com")
    phone = models.CharField( max_length=20)
    image = models.ImageField(upload_to="coaches/")

    
    def get_absolute_url(self):
        return reverse('coaches:coach-detail', args=[str(self.id)])


    def __str__(self):
        return self.name