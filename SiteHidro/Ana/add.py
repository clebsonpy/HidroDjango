from django.forms import forms
from Site.models import *

p = Reducao(Tipo="Maxima")
p.save(force_insert=True)