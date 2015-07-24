# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie_temporal',
            name='Data_e_Hora',
            field=models.CharField(max_length=25),
        ),
    ]
