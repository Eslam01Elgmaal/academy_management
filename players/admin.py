from django.contrib import admin
from .models import Player

# Register your models here.

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name','addras','image','birth_date',)
    technecal = ('dribbling','passing','shooting','Pace','Defense','Physical')

admin.site.register(Player, PlayerAdmin)