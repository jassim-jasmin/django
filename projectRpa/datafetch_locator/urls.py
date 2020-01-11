from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('layer/', views.getAllLayer, name='allLayer'),
    path('layer/<str:layer_id>/', views.layerData, name='layerData'),

]