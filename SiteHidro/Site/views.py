from django.shortcuts import render
from .models import Reducao

def inserir():
    p = Reducao(Tipo="Maxima")
    p.save(force_insert=True)