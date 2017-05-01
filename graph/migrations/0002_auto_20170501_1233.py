# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='name',
            field=models.CharField(default=b'', unique=True, max_length=200),
        ),
        migrations.AlterUniqueTogether(
            name='graphlinks',
            unique_together=set([('graph', 'link')]),
        ),
        migrations.AlterUniqueTogether(
            name='links',
            unique_together=set([('from_node', 'to_node')]),
        ),
    ]
