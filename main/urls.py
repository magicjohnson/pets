from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^cats/$', views.CatListView.as_view(), name='cat-list'),
    # url(r'^dogs/$', views.DogListView.as_view(), name='dog-list'),
    # url(r'^animals/$', views.AnimalListView.as_view(), name='animal-list'),
    url(r'^cats/$', views.PetListView.as_view(pet_category='cat'), name='cat-list'),
    url(r'^dogs/$', views.PetListView.as_view(pet_category='dog'), name='dog-list'),
    url(r'^animals/$', views.PetListView.as_view(pet_category='bird'), name='animal-list'),
    url(r'pets/(?P<slug>[\w-]+)-(?P<object_id>\d+)', views.PetDetailView.as_view(), name='pet-detail')
)
