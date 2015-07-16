# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20150701_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='friend',
            field=models.ForeignKey(related_name='referal', blank=b'True', to='core.Join', null=b'True'),
        ),
    ]
