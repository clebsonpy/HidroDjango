from django.contrib import admin
from .models import *

class Admin(admin.ModelAdmin):
    pass
admin.site.register(Serie_Original, Admin)
admin.site.register(Serie_Reduzida, Admin)
admin.site.register(Serie_Temporal, Admin)
admin.site.register(Posto, Admin)
admin.site.register(Tipo_Posto, Admin)
admin.site.register(Discretizacao, Admin)
admin.site.register(Reducao, Admin)
admin.site.register(Variavel, Admin)
admin.site.register(Localizacao, Admin)
admin.site.register(Nivel_Consistencia, Admin)
admin.site.register(Unidade, Admin)
admin.site.register(Fonte, Admin)