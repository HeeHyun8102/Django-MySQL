from django.urls import path

from . import views

urlpatterns = [
    path('', views.final, name='index'),
    #path('/search', views.final, name='search')
]