# -*- coding: utf-8 -*-

from django.views import generic
from main.models import Pet
from main.forms import SearchForm
from main import utils


class HomeView(generic.TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['form'] = SearchForm()
        return context


class PetDetailView(generic.DetailView):
    template_name = 'pet_detail.html'
    model = Pet


class PetListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 12
    CATEGORY = None
    CATEGORY_VERBOSE = None

    def get_context_data(self, **kwargs):
        css_class = {
            0: 'cat',
            1: 'dog',
            2: 'bird'
        }

        context = super(PetListView, self).get_context_data(**kwargs)
        if self.CATEGORY:
            context['pet_category'] = css_class[self.CATEGORY]
        else:
            context['pet_category'] = css_class[2]

        context['pet_category_verbose'] = self.CATEGORY_VERBOSE
        return context

    def get_queryset(self):
        filters = {'visible': True}
        if self.CATEGORY is not None:
            filters['animal'] = self.CATEGORY

        return Pet.objects.filter(**filters)


class CatListView(PetListView):
    CATEGORY = Pet.CAT
    CATEGORY_VERBOSE = u'Кошки'


class DogListView(PetListView):
    CATEGORY = Pet.DOG
    CATEGORY_VERBOSE = u'Собаки'


class AnimalListView(PetListView):
    CATEGORY = Pet.OTHER
    CATEGORY_VERBOSE = u'Другие животные'


class PetSearchView(PetListView):
    CATEGORY_VERBOSE = u'Результаты поиска'
    
    def get_queryset(self):
        filters = {}
        form = SearchForm(self.request.GET)
        if form.is_valid():
            if form.cleaned_data.get('animal') != '':
                filters['animal'] = form.cleaned_data.get('animal')

            if form.cleaned_data.get('sex') != '':
                filters['sex'] = form.cleaned_data.get('sex')

            if form.cleaned_data.get('city') != '':
                filters['foster_parent__city'] = form.cleaned_data.get('city')

            from_age = form.cleaned_data.get('from_age')
            from_age_units = form.cleaned_data.get('from_age_units')
            if from_age != '' and from_age_units != '':
                filters['birthday__gt'] = utils.get_birthdate(from_age, from_age_units)

            to_age = form.cleaned_data.get('to_age')
            to_age_units = form.cleaned_data.get('to_age_units')
            if to_age != '' and to_age_units != '':
                filters['birthday__lt'] = utils.get_birthdate(to_age, to_age_units)
            
            filters.update(filters)

        return Pet.objects.filter(**filters)

