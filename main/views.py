# -*- coding: utf-8 -*-

from django.views import generic
from django.template import RequestContext
from django.shortcuts import render_to_response
from main.models import Pet


class HomeView(generic.TemplateView):
    template_name = 'home.html'


# class CatListView(generic.ListView):
#     model = Pet
#     context_object_name = 'pets'
#     template_name = 'pet_list.html'
#     paginate_by = 10

#     def get_queryset(self):
#         return Pet.objects.filter(animal=Pet.CAT)


# class DogListView(generic.ListView):
#     model = Pet
#     context_object_name = 'pets'
#     template_name = 'pet_list.html'
#     paginate_by = 10

#     def get_queryset(self):
#         return Pet.objects.filter(animal=Pet.DOG)


# class AnimalListView(generic.ListView):
#     model = Pet
#     context_object_name = 'pets'
#     template_name = 'pet_list.html'
#     paginate_by = 10

#     def get_queryset(self):
#         return Pet.objects.filter(animal=Pet.OTHER)


class PetListView(generic.View):
    response_template = 'pet_list.html'
    pet_category = None

    def get(self, request, *args, **kwargs):
        context = locals()
        if self.pet_category == 'cat':
            context['pet_category'] = self.pet_category
            context['pet_category_verbose'] = 'Кошки'
            context['pets'] = Pet.objects.filter(animal=Pet.CAT)
        elif self.pet_category == 'dog':
            context['pet_category'] = self.pet_category
            context['pet_category_verbose'] = 'Собаки'
            context['pets'] = Pet.objects.filter(animal=Pet.DOG)
        else:
            context['pet_category'] = self.pet_category
            context['pet_category_verbose'] = 'Другие животные'
            context['pets'] = Pet.objects.filter(animal=Pet.OTHER)
            
        return render_to_response(self.response_template, context, context_instance=RequestContext(request))


class PetDetailView(generic.DetailView):
    template_name = 'pet_detail.html'
    model = Pet
