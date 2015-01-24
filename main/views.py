# -*- coding: utf-8 -*-

from django.views import generic
from main.models import Pet
from main.forms import SearchForm


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
    paginate_by = 10
    CATEGORY = None
    CATEGORY_VERBOSE = None

    def get_context_data(self, **kwargs):
        css_class = {
            0: 'cat',
            1: 'dog',
            2: 'bird'
        }

        context = super(PetListView, self).get_context_data(**kwargs)
        context['pet_category'] = css_class[self.CATEGORY]
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
