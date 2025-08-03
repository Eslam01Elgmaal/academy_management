from django.shortcuts import render
from .models import Paernt
from django.views.generic import ListView , DetailView
# Create your views here.

class PaerntList(ListView):
    model = Paernt
    context_object_name = 'paernt'
    template_name='paernts/paernt_list.html'



class PaerntDetail(DetailView):
    model = Paernt
    template_name='paernts/paernt_detail.html'

