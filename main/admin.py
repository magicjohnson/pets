from django import forms
from django.contrib import admin
from django.contrib.auth import get_permission_codename

from ckeditor.widgets import CKEditorWidget

from main import models


class PerObjectAccessAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        opts = self.opts
        codename = get_permission_codename('change', opts)
        return request.user.has_perm("%s.%s" % (opts.app_label, codename), obj)


class ImagesInline(admin.TabularInline):
    model = models.Image
    fk_name = 'pet'


class PetAdminForm(forms.ModelForm):
    history = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = models.Pet
        fields = '__all__'

@admin.register(models.Pet)
class PetAdmin(PerObjectAccessAdmin):
    form = PetAdminForm
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

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'foster_parent' and not request.user.is_superuser:
            kwargs['queryset'] = models.FosterParent.objects.filter(user=request.user)

        return super(PetAdmin, self).formfield_for_foreignkey(db_field, request=request, **kwargs)

    def get_changelist(self, request, **kwargs):
        from django.contrib.admin.views.main import ChangeList

        class FilteredPetsChangeList(ChangeList):
            def get_queryset(self, request):
                qs = super(FilteredPetsChangeList, self).get_queryset(request)
                if not request.user.is_superuser:
                    qs = qs.filter(foster_parent__user_id=request.user.id)
                return qs

        return FilteredPetsChangeList


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

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_changelist(self, request, **kwargs):
        from django.contrib.admin.views.main import ChangeList

        class FilteredParentsChangeList(ChangeList):
            def get_queryset(self, request):
                qs = super(FilteredParentsChangeList, self).get_queryset(request)
                if not request.user.is_superuser:
                    qs = qs.filter(user_id=request.user.id)
                return qs

        return FilteredParentsChangeList
