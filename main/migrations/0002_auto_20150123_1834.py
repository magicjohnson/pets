# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='size',
            field=models.PositiveIntegerField(default=1, verbose_name='\u0420\u0430\u0437\u043c\u0435\u0440', choices=[(0, '\u041c\u0430\u043b\u0435\u043d\u044c\u043a\u0438\u0439'), (1, '\u0421\u0440\u0435\u0434\u043d\u0438\u0439'), (2, '\u0411\u043e\u043b\u044c\u0448\u043e\u0439')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2015, 1, 23, 18, 34, 37, 968307, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
