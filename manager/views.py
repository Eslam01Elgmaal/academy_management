from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Manager

# Create your views here.


class Manager_detail(DetailView):
    model = Manager
    template_name = 'manager/manager_detail.html'
    context_object_name = 'manager'
