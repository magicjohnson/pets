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
        filters = {'visible': True}
        form = SearchForm(self.request.GET)
        form.is_valid()
        cleaned_data = form.clean()
        form_filters = {
            'animal': cleaned_data.get('animal'),
            'sex': cleaned_data.get('sex'),
            'foster_parent__city': cleaned_data.get('city')
        }

        from_age = cleaned_data.get('from_age')
        from_age_units = cleaned_data.get('from_age_units')
        if from_age and from_age_units:
            form_filters['birthday__lte'] = utils.get_birthdate(from_age, from_age_units)

        to_age = cleaned_data.get('to_age')
        to_age_units = cleaned_data.get('to_age_units')
        if to_age and to_age_units:
            form_filters['birthday__gte'] = utils.get_birthdate(to_age, to_age_units)
        
        filters_cleaned  = {k:v for k,v in form_filters.iteritems() if v}
        filters.update(filters_cleaned)

        return Pet.objects.filter(**filters)

