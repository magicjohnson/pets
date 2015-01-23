# coding=utf-8
from django.db import models
from sorl.thumbnail import ImageField


class FosterParent(models.Model):
    KARAGANDA = 0
    TEMIRTAU = 1

    CITY_CHOICES = (
        (KARAGANDA, u'Караганда'),
        (TEMIRTAU, u'Темиртау')
    )
    name = models.CharField(max_length=200, verbose_name=u'Имя')
    phone = models.CharField(max_length=200, verbose_name=u'Телефон')
    city = models.PositiveSmallIntegerField(choices=CITY_CHOICES, verbose_name=u'Город')


class Pet(models.Model):
    MALE = 0
    FEMALE = 1
    SEX_CHOICES = (
        (MALE, u'Самец'),
        (FEMALE, u'Самка'),
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
    age = models.PositiveIntegerField(verbose_name=u'Возраст')
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, verbose_name=u'Пол')
    breed = models.CharField(max_length=500, verbose_name=u'Порода')
    color = models.CharField(max_length=200, verbose_name=u'Цвет')
    vaccinated = models.BooleanField(default=False, verbose_name=u'Привит')
    sterilized = models.BooleanField(default=False, verbose_name=u'Стериализован')
    dewormed = models.BooleanField(default=False, verbose_name=u'Без паразитов')
    foster_parent = models.ForeignKey(FosterParent, verbose_name=u'Временный опекун')
    history = models.TextField(verbose_name=u'История')


class Image(models.Model):
    image = ImageField(upload_to='uploads/images')
    image_url = models.CharField(max_length=255, null=True, blank=True)
    pet = models.ForeignKey(Pet)
