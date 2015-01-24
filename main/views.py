# -*- coding: utf-8 -*-

from django.views import generic

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


class CatListView(PetListView):
    queryset = Pet.objects.filter(animal=Pet.CAT)


class DogListView(PetListView):
    queryset = Pet.objects.filter(animal=Pet.DOG)


class AnimalListView(PetListView):
    queryset = Pet.objects.filter(animal=Pet.OTHER)

