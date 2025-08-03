import random
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from datetime import date

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=70)
    addras = models.CharField(max_length=150)
    birth_date = models.DateField()
    image = models.ImageField( upload_to='players/')
    code = models.CharField(max_length=5, unique=True, editable=False)
    dribbling = models.IntegerField(validators=[MaxValueValidator(100)])
    passing = models.IntegerField(validators=[MaxValueValidator(100)])
    shooting = models.IntegerField(validators=[MaxValueValidator(100)])
    Pace = models.IntegerField(validators=[MaxValueValidator(100)])
    Defense = models.IntegerField(validators=[MaxValueValidator(100)])
    Physical = models.IntegerField(validators=[MaxValueValidator(100)])

    over_rating = models.IntegerField(blank=True, null=True)

    @property
    def age(self):
        today = date.today()
        delta = today - self.birth_date
        years = delta.days // 365
        days = delta.days % 365
        return f"{years} years and {days} days"


    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.generate_unique_code()
    
        self.over_rating = round(
            self.Pace * 0.2 +
            self.shooting * 0.25 +
            self.passing * 0.15 +
            self.dribbling * 0.2 +
            self.Defense * 0.1 +
            self.Physical * 0.1
        )

        super().save(*args, **kwargs)


    def generate_unique_code(self):
        while True:
            code = str(random.randint(0, 99999)).zfill(4)  
            if not Player.objects.filter(code=code).exists():
                return code

    def __str__(self):
        return self.name
