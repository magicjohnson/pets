# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150123_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='age',
        ),
        migrations.AddField(
            model_name='pet',
            name='birthday',
            field=models.DateField(default=datetime.datetime.now() - datetime.timedelta(days=10),
                                   verbose_name='\u0414\u0435\u043d\u044c \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f'),
            preserve_default=False,
        ),
    ]
