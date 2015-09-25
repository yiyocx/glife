# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_documentvote'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='documentvote',
            unique_together=set([('document', 'owner')]),
        ),
    ]
