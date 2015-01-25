# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

from sorl.thumbnail import ImageField
from permission import add_permission_logic
from permission.logics import AuthorPermissionLogic

from main import utils


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
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Опекун'
        verbose_name_plural = u'Опекуны'


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

    STATUS_CHOICES = (
        (0, u'у опекуна'),
        (1, u'нашел хозяина')
    )

    SMALL = 0
    MEDIUM = 1
    LARGE = 2
    SIZE_CHOICES = (
        (SMALL, u'Маленький'),
        (MEDIUM, u'Средний'),
        (LARGE, u'Большой'),
    )

    animal = models.PositiveSmallIntegerField(choices=ANIMAL_CHOICES, verbose_name=u'Вид животного')
    name = models.CharField(max_length=200, verbose_name=u'Кличка')
    birthday = models.DateField(validators=[utils.validate_birthday], verbose_name=u'День рождения')
    sex = models.PositiveSmallIntegerField(choices=SEX_CHOICES, verbose_name=u'Пол')
    breed = models.CharField(max_length=500, verbose_name=u'Порода')
    color = models.CharField(max_length=200, verbose_name=u'Цвет')
    vaccinated = models.BooleanField(default=False, verbose_name=u'Привит')
    sterilized = models.BooleanField(default=False, verbose_name=u'Стериализован')
    dewormed = models.BooleanField(default=False, verbose_name=u'Без паразитов')
    foster_parent = models.ForeignKey(FosterParent, verbose_name=u'Временный опекун')
    history = models.TextField(verbose_name=u'История')
    size = models.PositiveIntegerField(choices=SIZE_CHOICES, default=MEDIUM, verbose_name=u'Размер')
    status = models.PositiveIntegerField(choices=STATUS_CHOICES, verbose_name=u'Статус')
    visible = models.BooleanField(default=False, verbose_name=u'Показать на сайте')
    slug = models.SlugField()

    def __unicode__(self):
        return "%s %s" % (self.get_animal_display(), self.name)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('pet-detail', args=[str(self.slug), str(self.pk)])

    class Meta:
        verbose_name = u'Животное'
        verbose_name_plural = u'Животные'

    @property
    def age(self):
        return utils.age(self.birthday)


class Image(models.Model):
    image = ImageField(upload_to='images', null=True, blank=True)
    image_url = models.CharField(max_length=255, null=True, blank=True)
    pet = models.ForeignKey(Pet)

    def get_absolute_url(self):
        if self.image_url:
            return self.image_url

        return self.image.image_url

add_permission_logic(
    Pet,
    AuthorPermissionLogic(
        field_name='foster_parent__user',
        any_permission=False,
        change_permission=True,
        delete_permission=False,
    )
)

add_permission_logic(
    FosterParent,
    AuthorPermissionLogic(
        field_name='user',
        any_permission=False,
        change_permission=True,
        delete_permission=False,
    )
)
