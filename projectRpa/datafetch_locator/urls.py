from django.urls import path

from . import views

app_name = 'datafetch_locator'
urlpatterns = [
    path('', views.index, name='index'),
    path('layer_main/', views.layerMain, name='layerMain'),
    path('locator_main/', views.locatorMain, name='locatorMain'),
    path('add_layer/', views.addLayer, name='add_layer'),
    path('add_locator/<str:layerName>/', views.addLocator, name='add_locator')

]