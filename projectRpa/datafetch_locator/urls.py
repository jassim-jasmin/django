from django.urls import path

from . import views

app_name = 'datafetch_locator'
urlpatterns = [
    path('', views.index, name='index'),
    path('layer_main/', views.layerMain, name='layerMain'),
    path('<str:layer>/', views.locatorMain, name='locatorMain')

]