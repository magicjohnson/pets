# -*- coding: utf-8 -*-

from datetime import datetime
from django import template
from main.models import Pet


register = template.Library()


@register.simple_tag
def we_helped():
    return Pet.objects.filter(status=1).count()
    