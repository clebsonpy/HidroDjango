# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discretizacao',
            fields=[
                ('Discretizacao_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('Fonte_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Fonte', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('Localizacao_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Latitude', models.CharField(max_length=10, null=True)),
                ('Longitude', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel_Consistencia',
            fields=[
                ('Tipo_Dado_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Nivel', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posto',
            fields=[
                ('Posto_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Codigo_ANA', models.CharField(max_length=20, null=True)),
                ('Fonte_ID', models.ForeignKey(to='Site.Fonte')),
                ('Localizacao_ID', models.ForeignKey(to='Site.Localizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Original',
            fields=[
                ('Serie_Original_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Arquivo_Fonte_Data', models.CharField(max_length=20)),
                ('Discretizacao_ID', models.ForeignKey(to='Site.Discretizacao')),
                ('Posto_ID', models.ForeignKey(to='Site.Posto')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Reduzida',
            fields=[
                ('Serie_Reduzida_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Discretizacao_ID', models.ForeignKey(to='Site.Discretizacao')),
            ],
        ),
        migrations.CreateModel(
            name='Serie_Temporal',
            fields=[
                ('Serie_Temporal_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Data_e_Hora', models.DateTimeField()),
                ('Dado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Posto',
            fields=[
                ('Tipo_Posto_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('Unidade_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='reducao',
            old_name='Reducao_id',
            new_name='Reducao_ID',
        ),
        migrations.RenameField(
            model_name='variavel',
            old_name='Variavel_id',
            new_name='Variavel_ID',
        ),
        migrations.AlterUniqueTogether(
            name='serie_temporal',
            unique_together=set([('Serie_Temporal_ID', 'Data_e_Hora')]),
        ),
        migrations.AddField(
            model_name='serie_reduzida',
            name='Reducao_ID',
            field=models.ForeignKey(to='Site.Reducao'),
        ),
        migrations.AddField(
            model_name='serie_reduzida',
            name='Serie_Original_ID',
            field=models.ForeignKey(to='Site.Serie_Original'),
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
