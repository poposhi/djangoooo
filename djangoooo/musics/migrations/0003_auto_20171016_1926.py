# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='Vavg',
            field=models.FloatField(default=64),
        ),
    ]
