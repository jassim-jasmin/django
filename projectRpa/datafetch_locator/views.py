from django.shortcuts import get_object_or_404, render, reverse
from django.http import Http404

from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from .models import Layer, Layer_Connect, Layer_Validation, Locator
from django.template import loader

def layerMain(request):
    layerName = Layer.objects.order_by('layer_name')
    layerJson = { 'layer_name' : layerName}

    return render(request, 'datafetch_locator/layer_main.html', layerJson)

def locatorMain(request):
    if 'layer' in request.POST:
        selectedLayer = Layer.objects.get(pk=request.POST['layer'])

        locator = Locator.objects.filter(layer_name=selectedLayer)

        locatorJson = {'locator' : selectedLayer, 'layer_name':selectedLayer}
    else:
        return render(request, 'datafetch_locator/locator_main.html', {'locator' : None})

    return render(request, 'datafetch_locator/locator_main.html', locatorJson)

def index(request):
    return HttpResponse('hello')

def addLayer(request):
    """
    For adding new layer
    :param request:
    :param layerName:
    :return:
    """
    input_layer_name = request.POST['input_layer_name']
    print('adding layer', input_layer_name)
    layer = Layer(layer_name=input_layer_name)
    layer.save()
    layer_list = Layer.objects.order_by

    # return HttpResponse('success')
    return render(request, 'datafetch_locator/layer_main.html', {
            'layer_name': layer_list,
    })

def addLocator(request, layerName):
    if 'add_locator_button' in request.POST:
        print('layer name', layerName)
        newLocator = request.POST['add_locator_button']
        locator = Locator.obje

    return HttpResponse('success')

def testFunction():
    print('button cliked')
#
# def deleteLayer(reques, layer_list):
#     print('delete layer')
#     return HttpResponse('success')