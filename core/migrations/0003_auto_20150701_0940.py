# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150630_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=b'ABC', max_length=50),
        ),
        migrations.AlterField(
            model_name='join',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
