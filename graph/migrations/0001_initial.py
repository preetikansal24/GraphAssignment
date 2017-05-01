# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('created_at', models.DateField(auto_now=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GraphLinks',
            fields=[
                ('created_at', models.DateField(auto_now=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('graph', models.ForeignKey(to='graph.Graph')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('created_at', models.DateField(auto_now=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('created_at', models.DateField(auto_now=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='links',
            name='from_node',
            field=models.ForeignKey(related_name='from_node', to='graph.Nodes'),
        ),
        migrations.AddField(
            model_name='links',
            name='to_node',
            field=models.ForeignKey(related_name='to_node', to='graph.Nodes'),
        ),
        migrations.AddField(
            model_name='graphlinks',
            name='link',
            field=models.ForeignKey(to='graph.Links'),
        ),
    ]
