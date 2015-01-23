from django.conf.urls import patterns, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.HomeView.as_view()),
    url(r'^cats/$', views.CatsView.as_view()),
    url(r'^dogs/$', views.DogsView.as_view()),
)
