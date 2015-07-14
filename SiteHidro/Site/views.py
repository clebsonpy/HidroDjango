from django.shortcuts import render
from .models import *

class CreateView():
    R = Reducao.objects.create(Tipo= 'Maximo')
