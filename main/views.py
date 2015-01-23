# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, ListView
# from django.views.decorators.csrf import csrf_protect
# from django.shortcuts import render_to_response
# from django.template import RequestContext
from models import Pet

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'


class CatsView(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=0)


class DogsView(ListView):
    model = Pet
    context_object_name = 'pets'
    template_name = 'pet_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Pet.objects.filter(animal=1)
        
