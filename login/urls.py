from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_main, name='login'),
    path('reg/', views.login_reg, name='register'),
]