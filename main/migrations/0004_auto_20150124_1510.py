# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150124_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='visible',
            field=models.BooleanField(default=False, verbose_name='\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430 \u0441\u0430\u0439\u0442\u0435'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'images', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(),
            preserve_default=True,
        ),
    ]
