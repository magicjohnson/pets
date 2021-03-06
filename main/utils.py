# coding=utf-8
from __future__ import unicode_literals

import datetime
from django.core.exceptions import ValidationError

from django.utils.translation import ugettext, ungettext_lazy


def age(d, now=None):
    chunks = (
        (365, ungettext_lazy('%d year', '%d years')),
        (30, ungettext_lazy('%d month', '%d months')),
        (7, ungettext_lazy('%d week', '%d weeks')),
    )

    if isinstance(d, datetime.datetime):
        d = datetime.date(d.year, d.month, d.day)
    if now and isinstance(now, datetime.datetime):
        now = datetime.date(now.year, now.month, now.day)

    if not now:
        now = datetime.date.today()

    delta = now - d
    since = delta.days

    if since <= 0:
        return 0

    count, i = 0, 0
    days, name = chunks[i]

    for i, (days, name) in enumerate(chunks):
        count = since // days
        if count != 0:
            break

    result = name % count

    if i + 1 < len(chunks):
        # Now get the second item
        days2, name2 = chunks[i + 1]
        count2 = (since - (days * count)) // days2
        if count2 != 0:
            result += ugettext(', ') + name2 % count2
    return result


def validate_birthday(date):
    if isinstance(date, datetime.datetime):
        date = datetime.date(year=date.year, month=date.month, day=date.day)

    today = date.today()
    delta = today - date
    if delta.days < 0:
        raise ValidationError(u'День рождения %s может быть только в прошлом' % date)


def get_birthdate(value, units, now=None):
    if now and isinstance(now, datetime.datetime):
        now = datetime.date(now.year, now.month, now.day)

    if not now:
        now = datetime.date.today()

    try:
        days_to_substract = int(units)*int(value)
    except Exception, e:
        return e
    else:
        birthdate = now - datetime.timedelta(days=days_to_substract)

        return birthdate
