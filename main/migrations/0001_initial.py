# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FosterParent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='\u0418\u043c\u044f')),
                ('phone', models.CharField(max_length=200, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('city', models.PositiveSmallIntegerField(verbose_name='\u0413\u043e\u0440\u043e\u0434', choices=[(0, '\u041a\u0430\u0440\u0430\u0433\u0430\u043d\u0434\u0430'), (1, '\u0422\u0435\u043c\u0438\u0440\u0442\u0430\u0443')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'uploads/images')),
                ('image_url', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('animal', models.PositiveSmallIntegerField(verbose_name='\u0412\u0438\u0434 \u0436\u0438\u0432\u043e\u0442\u043d\u043e\u0433\u043e', choices=[(0, '\u041a\u043e\u0448\u043a\u0430'), (1, '\u0421\u043e\u0431\u0430\u043a\u0430'), (2, '\u0414\u0440\u0443\u0433\u043e\u0435')])),
                ('name', models.CharField(max_length=200, verbose_name='\u041a\u043b\u0438\u0447\u043a\u0430')),
                ('age', models.PositiveIntegerField(verbose_name='\u0412\u043e\u0437\u0440\u0430\u0441\u0442')),
                ('sex', models.PositiveSmallIntegerField(verbose_name='\u041f\u043e\u043b', choices=[(0, '\u0421\u0430\u043c\u0435\u0446'), (1, '\u0421\u0430\u043c\u043a\u0430')])),
                ('breed', models.CharField(max_length=500, verbose_name='\u041f\u043e\u0440\u043e\u0434\u0430')),
                ('color', models.CharField(max_length=200, verbose_name='\u0426\u0432\u0435\u0442')),
                ('vaccinated', models.BooleanField(default=False, verbose_name='\u041f\u0440\u0438\u0432\u0438\u0442')),
                ('sterilized', models.BooleanField(default=False, verbose_name='\u0421\u0442\u0435\u0440\u0438\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u043d')),
                ('dewormed', models.BooleanField(default=False, verbose_name='\u0411\u0435\u0437 \u043f\u0430\u0440\u0430\u0437\u0438\u0442\u043e\u0432')),
                ('history', models.TextField(verbose_name='\u0418\u0441\u0442\u043e\u0440\u0438\u044f')),
                ('foster_parent', models.ForeignKey(verbose_name='\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u044b\u0439 \u043e\u043f\u0435\u043a\u0443\u043d', to='main.FosterParent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='image',
            name='pet',
            field=models.ForeignKey(to='main.Pet'),
            preserve_default=True,
        ),
    ]
