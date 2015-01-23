# -*- coding: utf-8 -*-

#from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Pet

# Create your views here.


# class HomeView(TemplateView):
#     template_name = 'home.html'


def HomeView(request):
	data_dict = {}
	return render_to_response('home.html', data_dict, context_instance=RequestContext(request))
