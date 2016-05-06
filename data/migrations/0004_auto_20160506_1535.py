# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-06 15:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_datarepository_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brainimage',
            name='basefilecollection_ptr',
        ),
        migrations.RemoveField(
            model_name='file',
            name='basefilecollection_ptr',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='basefilecollection_ptr',
        ),
        migrations.RemoveField(
            model_name='timeseries',
            name='basefilecollection_ptr',
        ),
        migrations.AlterModelOptions(
            name='archivedatarepository',
            options={'verbose_name_plural': 'archive data repositories'},
        ),
        migrations.AlterModelOptions(
            name='datarepository',
            options={'verbose_name_plural': 'data repositories'},
        ),
        migrations.AlterModelOptions(
            name='localdatarepository',
            options={'verbose_name_plural': 'local data repositories'},
        ),
        migrations.AlterModelOptions(
            name='networkdatarepository',
            options={'verbose_name_plural': 'network data repositories'},
        ),
        migrations.DeleteModel(
            name='BrainImage',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='TimeSeries',
        ),
    ]
