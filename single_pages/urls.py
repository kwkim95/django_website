from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about_me/', views.about_me),
]