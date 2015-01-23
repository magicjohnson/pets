from django.contrib import admin

from main import models


class ImagesInline(admin.TabularInline):
    model = models.Image
    fk_name = 'pet'


@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'age',
        'sex',
        'breed',
        'color',
        'vaccinated',
        'sterilized',
        'dewormed',
        'foster_parent',
        'status',
    )

    list_filter = (
        'animal',
        'sex',
        'foster_parent',
        'status',
    )

    inlines = (
        ImagesInline,
    )


@admin.register(models.FosterParent)
class FosterParent(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'city',
    )

    list_filter = (
        'city',
    )


