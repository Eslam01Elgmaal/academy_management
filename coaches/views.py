from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Coaches

# Create your views here.

class CoachesList(ListView):
    model = Coaches
    template_name = 'coaches/coaches_list.html'
    context_object_name = 'coach'


class CoachesDetail(DetailView):
    model = Coaches
    template_name='coaches/coaches_detail.html'
    context_object_name = 'coach'