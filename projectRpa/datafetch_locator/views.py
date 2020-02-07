from django.shortcuts import get_object_or_404, render, reverse
from django.http import Http404

from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from .models import Layer, Layer_Connect, Layer_Validation, Locator
from django.template import loader

def layerMain(request):
    try:
        layerName = Layer.objects.order_by('layer_name')
        layerConnect = Layer_Connect.objects.order_by('id')
        layerJson = { 'layer_name' : layerName, 'layer_connect':layerConnect}

        return render(request, 'datafetch_locator/layer_main.html', layerJson)
    except Exception as e:
        return render(request, 'datafetch_locator/layer_main.html', {'error_message':e})

def locatorMain(request):
    if 'delete_layer_button' in request.POST:
        layer = Layer.objects.get(pk=request.POST['layer'])
        layer.delete()
        print('deleted',layer)
        layerName = Layer.objects.order_by('layer_name')
        layerJson = {'layer_name': layerName}
        return render(request, 'datafetch_locator/layer_main.html', layerJson)
    else:
        if 'layer' in request.POST:
            selectedLayer = Layer.objects.get(pk=request.POST['layer'])
            locatorList = selectedLayer.locator_set.all()
            locatorJson = {'locator' : selectedLayer, 'layer_name':selectedLayer, 'locator_list':locatorList}
        else:
            locatorJson = {'locator' : None}

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
        locatorId = request.POST['locator_id']
        locatorTag = request.POST['locator_tag']
        layer = Layer.objects.get(layer_name=layerName)

        layer.locator_set.create(layer_name=layerName, locator_id=locatorId, locator_data=locatorTag)
        locatorList = layer.locator_set
        locatorJson = {'locator' : layerName, 'layer_name':layerName, 'locator_list':locatorList}
    else:
        locatorJson = {'locator' : None}

    return render(request, 'datafetch_locator/locator_main.html', locatorJson)

    # return HttpResponse(layer.locator_set.all())

def deleteLocatorData(request):
    if 'delete_locator_tag' in request.POST:
        locator = Locator.objects.get(id=request.POST['locator_tag'])
        layerName = locator.layer_name
        locator.delete()
        layer = Layer.objects.get(layer_name=layerName)
        locatorJson = {'locator': layerName, 'layer_name': layerName, 'locator_list': layer.locator_set}

    else:
        locatorJson = {'locator': None}

    return render(request, 'datafetch_locator/locator_main.html', locatorJson)

def layerConnectorMain(request):
    print('hello')
    return HttpResponse('hello')

def testFunction():
    print('button cliked')
#
# def deleteLayer(reques, layer_list):
#     print('delete layer')
#     return HttpResponse('success')