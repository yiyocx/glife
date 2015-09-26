# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20150925_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentvote',
            name='document',
            field=models.ForeignKey(to='api.Document'),
        ),
    ]
