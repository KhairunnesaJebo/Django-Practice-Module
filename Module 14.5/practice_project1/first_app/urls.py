from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "homepage"),
    path('django_form/', views.example_form, name = "django_form"),
]
