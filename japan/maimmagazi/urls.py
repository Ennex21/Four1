from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('categ2/', views.categ2, name='categ2'),
    path('categ3/', views.categ3, name='categ3'),
    path('categ4/', views.categ4, name='categ4'),
    path('categ5/', views.categ5, name='categ5'),
    path('categ6/', views.categ6, name='categ6'),
    path('categ7/', views.categ7, name='categ7'),
    path('Registrat/', views.Registrat, name='Registrat'),
]