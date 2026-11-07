
from django.urls import path
from . import views

urlpatterns = [
    path('Hola-mundo/', views.index, name='index'),
    path('instructor/', views.instructor, name='instructor'),
    path('curso/', views.curso, name='curso'),
    path('ficha/', views.ficha, name='ficha'),
    path('centro/', views.centro, name='centro'),
    path('inicio/', views.inicio, name='inicio'),
]
