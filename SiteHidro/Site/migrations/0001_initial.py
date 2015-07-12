# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reducao',
            fields=[
                ('Reducao_id', models.AutoField(serialize=False, primary_key=True)),
                ('Tipo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Variavel',
            fields=[
                ('Variavel_id', models.AutoField(serialize=False, primary_key=True)),
                ('Variavel', models.CharField(max_length=20)),
            ],
        ),
    ]
