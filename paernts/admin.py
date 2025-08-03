from django.contrib import admin
from .models import Paernt

# Register your models here.

class PaerntAdmin(admin.ModelAdmin):
    list_display = ('addres','name')


admin.site.register(Paernt, PaerntAdmin)