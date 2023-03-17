from django.urls import path, re_path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('films/', views.films_main, name='films'),
    path('subscription/', views.subscription, name='subscription'),
    path('docs/', views.docs, name='docs'),
    path('profile/', views.profile, name='profile'),
    re_path(r'^film/(?P<id>\d+)$', views.films_film, name='film')
]