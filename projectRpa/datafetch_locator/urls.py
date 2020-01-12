from django.urls import path

from . import views

app_name = 'datafetch_locator'
urlpatterns = [
    path('', views.index, name='index'),
    path('layer/', views.getAllLayer, name='allLayer'),
    path('layer/<str:layer_id>/', views.layerData, name='layerData'),
    path('<str:locator_id>/', views.manage_locator, name='manage_locator'),
    path('/', views.addLayer, name='add_layer')

]