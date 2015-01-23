# -*- coding: utf-8 -*-

from django.views import generic

from main.models import Pet


class HomeView(generic.TemplateView):
    template_name = 'home.html'


class CatListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=0)


class DogListView(generic.ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=Pet.DOG)


class PetDetailView(generic.DetailView):
    template_name = 'pet_detail.html'
    model = Pet
