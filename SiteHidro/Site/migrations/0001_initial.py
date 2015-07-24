# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discretizacao',
            fields=[
                ('Discretizacao_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('Fonte_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Fonte', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('Localizacao_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Latitude', models.CharField(null=True, max_length=10)),
                ('Longitude', models.CharField(null=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Consistencia',
            fields=[
                ('Tipo_Dado_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Nivel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('Posto_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Codigo_ANA', models.CharField(null=True, max_length=20)),
                ('Fonte_ID', models.ForeignKey(to='Site.Fonte')),
                ('Localizacao_ID', models.ForeignKey(to='Site.Localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Reducao',
            fields=[
                ('Reducao_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Original',
            fields=[
                ('Serie_Original_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Arquivo_Fonte_Data', models.CharField(max_length=20)),
                ('Discretizacao_ID', models.ForeignKey(to='Site.Discretizacao')),
                ('Posto_ID', models.ForeignKey(to='Site.Posto')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Reduzida',
            fields=[
                ('Serie_Reduzida_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Discretizacao_ID', models.ForeignKey(to='Site.Discretizacao')),
                ('Reducao_ID', models.ForeignKey(to='Site.Reducao')),
                ('Serie_Original_ID', models.ForeignKey(to='Site.Serie_Original')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Temporal',
            fields=[
                ('Serie_Temporal_ID', models.IntegerField(serialize=False, primary_key=True)),
                ('Data_e_Hora', models.CharField(max_length=15)),
                ('Dado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Posto',
            fields=[
                ('Tipo_Posto_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('Unidade_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Variavel',
            fields=[
                ('Variavel_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Variavel', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='serie_temporal',
            unique_together=set([('Serie_Temporal_ID', 'Data_e_Hora')]),
        ),
        migrations.AddField(
            model_name='serie_reduzida',
            name='Serie_Temporal_ID',
            field=models.ForeignKey(to='Site.Serie_Temporal'),
        ),
        migrations.AddField(
            model_name='serie_original',
            name='Serie_Temporal_ID',
            field=models.ForeignKey(to='Site.Serie_Temporal'),
        ),
        migrations.AddField(
            model_name='serie_original',
            name='Tipo_Dado_ID',
            field=models.ForeignKey(to='Site.Nivel_Consistencia'),
        ),
        migrations.AddField(
            model_name='serie_original',
            name='Unidade_ID',
            field=models.ForeignKey(to='Site.Unidade'),
        ),
        migrations.AddField(
            model_name='serie_original',
            name='Variavel_ID',
            field=models.ForeignKey(to='Site.Variavel'),
        ),
        migrations.AddField(
            model_name='posto',
            name='Tipo_Posto_ID',
            field=models.ForeignKey(to='Site.Tipo_Posto'),
        ),
    ]
