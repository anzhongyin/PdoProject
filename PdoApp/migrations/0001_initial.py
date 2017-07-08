# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admincheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('admin', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=3)),
                ('sex', models.CharField(max_length=2)),
                ('grade', models.CharField(max_length=10)),
                ('major', models.CharField(max_length=30)),
                ('personinformation', models.CharField(max_length=100)),
                ('map', models.CharField(max_length=100)),
            ],
        ),
    ]
