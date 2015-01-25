# -*- coding: utf-8 -*-

from django import forms
from main.models import Pet, FosterParent


class SearchForm(forms.Form):
    WEEKS = 7
    MONTHS = 30
    YEARS = 365

    UNIT_CHOICES = (
        (WEEKS, u'Недель'),
        (MONTHS, u'Месяцев'),
        (YEARS, u'Лет')
    )

    ANIMAL_CHOICES_WITH_ANY = (('', u'Любое животное'),) + Pet.ANIMAL_CHOICES
    SEX_CHOICES_WITH_ANY = (('', u'Любой пол'),) + Pet.SEX_CHOICES
    CITY_CHOICES_WITH_ANY = (('', u'Любой город'),) + FosterParent.CITY_CHOICES

    animal = forms.CharField(
        widget=forms.Select(
            choices=ANIMAL_CHOICES_WITH_ANY,
            attrs={
                'id': 'params_category',
                'class': 'form-control',
                'name': 'params[category]'
                }
        ),
        label=u"Вид животного",
        required=False
    )
    sex = forms.CharField(
        widget=forms.Select(
            choices=SEX_CHOICES_WITH_ANY,
            attrs={
                'id': 'params_sex',
                'class': 'form-control',
                'name': 'params[sex]'
            }
        ),
        label=u"Пол",
        required=False
    )
    from_age = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                'id': 'params_ageFrom',
                'name': 'params[ageFrom]'
            }
        ),
        min_value=1,
        label=u"от",
        required=False
    )
    from_age_units = forms.CharField(
        widget=forms.Select(
            choices=UNIT_CHOICES,
            attrs={
                'id': 'params_ageFromUnit',
                'class': 'form-control',
                'name': 'params[ageFromUnit]'
            }
        ),
        required=False
    )
    to_age = forms.IntegerField(
    	widget=forms.TextInput(
            attrs={
                'id': 'params_ageTo',
                'name': 'params[ageTo]'
            }
        ),
        min_value=1,
        label=u"до",
        required=False
    )
    to_age_units = forms.CharField(
        widget=forms.Select(
            choices=UNIT_CHOICES,
            attrs={
                'id': 'params_ageToUnit',
                'class': 'form-control',
                'name': 'params[ageToUnit]'
            }
        ),
        required=False
    )
    city = forms.CharField(
        widget=forms.Select(
            choices=CITY_CHOICES_WITH_ANY,
            attrs={
                'id': 'params_city',
                'class': 'form-control',
                'name': 'params[city]'
            }
        ),
        label=u"Город",
        required=False
    )
