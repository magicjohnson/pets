from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^cats/$', views.CatListView.as_view(), name='cat-list'),
    url(r'^dogs/$', views.DogListView.as_view(), name='dog-list'),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'pets/(?P<slug>[\w-]+)', views.PetDetailView.as_view(), name='pet-detail')
)
