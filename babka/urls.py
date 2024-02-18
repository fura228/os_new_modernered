from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('tovar/<int:tovar_id>/', categories, name='tovar'),
    path('about', about, name='about')
]
