from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('films/', views.films_main, name='films'),
    re_path(r'^film/(?P<id>\d+)$', views.films_film, name='film'),
]