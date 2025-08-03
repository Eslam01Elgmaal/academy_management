from django.contrib import admin
from .models import Coaches

# Register your models here.

class CoacheAdmin(admin.ModelAdmin):
    list_display = ('job_title','name', 'email', 'phone','image')


admin.site.register(Coaches, CoacheAdmin)