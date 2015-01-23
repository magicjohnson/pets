# coding=utf-8
from django.db import models


class FosterParent(models.Model):
    name = models.CharField(max_length=200, verbose_name=u'Имя')
    phone = models.CharField(max_length=200, verbose_name=u'Телефон')


class Pet(models.Model):
    MALE = 0
    FEMALE = 1
    SEX_CHOICES = (
        (MALE,  u'Мужской'),
        (FEMALE, u'Женский'),
    )

    CAT = 0
    DOG = 1
    OTHER = 2
    ANIMAL_CHOICES = (
        (CAT, u'Кошка'),
        (DOG, u'Собака'),
        (OTHER, u'Другое'),
    )

    animal = models.PositiveSmallIntegerField(choices=ANIMAL_CHOICES, verbose_name=u'Вид животного')
    name = models.CharField(max_length=200, verbose_name=u'Кличка')

    age = models.IntegerField(verbose_name=u'Возраст')
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, verbose_name=u'Пол')
    breed = models.CharField(max_length=500, verbose_name=u'Порода')
    color = models.CharField(max_length=200, verbose_name=u'Цвет')
    vaccinated = models.BooleanField(verbose_name=u'Привит')
    sterilized = models.BooleanField(verbose_name=u'Стериализован')
    dewormed = models.BooleanField(verbose_name=u'Без паразитов')
    foster_parent = models.ForeignKey(FosterParent, verbose_name=u'Временный опекун')
    history = models.TextField(verbose_name=u'История')


