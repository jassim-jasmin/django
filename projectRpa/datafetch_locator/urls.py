from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:locator_id>/', views.getLocatorId),
    path('<str:layer_id>/layer_id', views.layerData)
]