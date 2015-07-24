from django.db import models
from django.utils import timezone
from numpy.lib.tests.test__datasource import teardown


class Reducao(models.Model):
    Reducao_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=10, null=False)

class Variavel(models.Model):
    Variavel_ID = models.AutoField(primary_key=True, null=False)
    Variavel = models.CharField(max_length=20, null= False)

class Fonte(models.Model):
    Fonte_ID = models.AutoField(primary_key=True, null=False)
    Fonte = models.CharField(max_length=20, null=False)

class Discretizacao(models.Model):
    Discretizacao_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=20, null=False)

class Tipo_Posto(models.Model):
    Tipo_Posto_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=20, null=False)

class Localizacao(models.Model):
    Localizacao_ID = models.AutoField(primary_key=True, null=False)
    Latitude = models.CharField(max_length=10, null=True)
    Longitude = models.CharField(max_length=10, null=True)

class Posto(models.Model):
    Posto_ID = models.AutoField(primary_key=True, null=False)
    Codigo_ANA = models.CharField(max_length=20, null=True)
    Fonte_ID = models.ForeignKey(Fonte)
    Localizacao_ID = models.ForeignKey(Localizacao)
    Tipo_Posto_ID = models.ForeignKey(Tipo_Posto)

class Nivel_Consistencia(models.Model):
    Tipo_Dado_ID = models.AutoField(primary_key=True, null=False)
    Nivel = models.CharField(max_length=20, null=False)

class Unidade(models.Model):
    Unidade_ID = models.AutoField(primary_key=True, null=False)
    Tipo = models.CharField(max_length=20, null=False)

class Serie_Temporal(models.Model):
    Serie_Temporal_ID = models.IntegerField(null=False)
    Data_e_Hora = models.CharField(max_length=25, null=False)
    Dado = models.CharField(max_length=10, null=False)
    class Meta:
        unique_together = ('Serie_Temporal_ID', 'Data_e_Hora')

class Serie_Original(models.Model):
    Serie_Original_ID = models.AutoField(primary_key=True, null=False)
    Arquivo_Fonte_Data = models.CharField(max_length=20, null=False)
    Serie_Temporal_ID = models.ManyToManyField(Serie_Temporal,
                                               through='Serie_Temporal',
                                               through_fields='Serie_Temporal_')
    Discretizacao_ID = models.ForeignKey(Discretizacao)
    Variavel_ID = models.ForeignKey(Variavel)
    Tipo_Dado_ID = models.ForeignKey(Nivel_Consistencia)
    Unidade_ID = models.ForeignKey(Unidade)
    Posto_ID = models.ForeignKey(Posto)

class Serie_Reduzida(models.Model):
    Serie_Reduzida_ID = models.AutoField(primary_key=True, null=False)
    Reducao_ID = models.ForeignKey(Reducao)
    Discretizacao_ID = models.ForeignKey(Discretizacao)
    Serie_Temporal_ID = models.ManyToManyField(Serie_Temporal,
                                               through='Serie_Temporal',
                                               through_fields='Serie_Temporal_ID')
    Serie_Original_ID = models.ForeignKey(Serie_Original)