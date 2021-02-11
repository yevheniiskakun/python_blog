from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from webpage import views

urlpatterns = [
    path('', views.index),
    path('date_sorted_old', views.index),
    path('date_sorted_new', views.index),
    path('name_sorted', views.index),
    path('last_three', views.index),
]