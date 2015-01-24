# -*- coding: utf-8 -*-

from django.views import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from main.models import Pet


class HomeView(generic.TemplateView):
    template_name = 'home.html'


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
        context = super(PetListView, self).get_context_data(**kwargs)
        context['pet_category'] = self.CATEGORY
        context['pet_category_verbose'] = self.CATEGORY_VERBOSE
        return context

    def get_queryset(self):
        if self.CATEGORY is not None:
            return Pet.objects.filter(animal=self.CATEGORY)

        return Pet.objects.all()


class CatListView(PetListView):
    CATEGORY = Pet.CAT
    CATEGORY_VERBOSE = u'Кошки'


class DogListView(PetListView):
    CATEGORY = Pet.DOG
    CATEGORY_VERBOSE = u'Собаки'


class AnimalListView(PetListView):
    CATEGORY = Pet.OTHER
    CATEGORY_VERBOSE = u'Другие животные'
