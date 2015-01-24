# -*- coding: utf-8 -*-

from django.views import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from main.models import Pet


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class CatListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=Pet.CAT)


class DogListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=Pet.DOG)

class CatListView(PetListView):
    queryset = Pet.objects.filter(animal=Pet.CAT)

class AnimalListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=Pet.OTHER)


class AnimalListView(PetListView):
    queryset = Pet.objects.filter(animal=Pet.OTHER)

