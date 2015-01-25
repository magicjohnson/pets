# coding=utf-8
from datetime import date, timedelta
from django.contrib.auth.models import User

import factory
from factory import fuzzy
from factory.django import DjangoModelFactory

from main import models


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ("username",)

    username = fuzzy.FuzzyText(prefix="test", length=4, chars="0123456789")
    password = factory.PostGenerationMethodCall('set_password', 'password')
    first_name = factory.Sequence(lambda n: "Firstname%s" % n)
    last_name = factory.Sequence(lambda n: "Lastname%s" % n)
    email = factory.LazyAttribute(lambda o: "test_%s@mail.xx" % o.username)
    is_staff = True
    is_active = True


class ImageFactory(DjangoModelFactory):
    class Meta:
        model = models.Image


class FosterParentFactory(DjangoModelFactory):
    class Meta:
        model = models.FosterParent
        django_get_or_create = ('user', )

    name = fuzzy.FuzzyText(prefix="foster", length=4, chars="0123456789")
    user = factory.SubFactory(UserFactory)
    city = models.FosterParent.KARAGANDA


class PetFactory(DjangoModelFactory):
    class Meta:
        model = models.Pet

    name = fuzzy.FuzzyText(prefix="pet", length=4, chars="0123456789")
    animal = fuzzy.FuzzyChoice([0, 1])
    sex = fuzzy.FuzzyChoice([0, 1])
    slug = factory.LazyAttribute(lambda o: o.name)
    birthday = fuzzy.FuzzyDate(
        start_date=date(2013, 01, 01),
        end_date=date.today() - timedelta(days=1)
    )
    status = 0
    visible = True

    foster_parent = factory.SubFactory(FosterParentFactory)



