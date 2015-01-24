from django.contrib import admin
from django.contrib.auth import get_permission_codename

from main import models


class PerObjectModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        opts = self.opts
        codename = get_permission_codename('change', opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename), obj)

    def has_add_permission(self, request):
        return request.user.is_staff


class ImagesInline(admin.TabularInline):
    model = models.Image
    fk_name = 'pet'


@admin.register(models.Pet)
class PetAdmin(PerObjectModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'foster_parent':
            kwargs['queryset'] = models.FosterParent.objects.filter(user=request.user)

        return super(PetAdmin, self).formfield_for_foreignkey(db_field, request=request, **kwargs)

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
    prepopulated_fields = {
        'slug': ('name',)
    }



@admin.register(models.FosterParent)
class FosterParent(admin.ModelAdmin):
    list_display = (
        'name',
        'phone',
        'city',
    )
    exclude = (
        'user',
    )
    list_filter = (
        'city',
    )

    def has_add_permission(self, request):
        return request.user.is_staff

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
