from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from .models import Layer, Locator
from django.template import loader

def index(request):
    """
    todo Need to perform other operation for index page
    :param request:
    :return:
    """
    layerArray = Layer.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': layerArray,
    }
    return render(request, 'datafetch_locator/index.html', context)

def getAllLayer(request):
    """
    Returns all layers available
    todo Change to profile wise layer
    :param request:
    :return: layer list in index.html
    """
    layerArray = Layer.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': layerArray,
    }
    return render(request, 'datafetch_locator/index.html', context)

def getLocatorId(request, locator_id):
    return HttpResponse("Locator id: %s" % locator_id)

def layerData(request, layer_id):
    """
    Purpose of this function is, based on layer_name corresponding locators need to return
    :param request:
    :param layer_id: layer name
    :return: locator coresponding layer
    """
    try:
        getLayer = get_object_or_404(Layer, layer_name=layer_id)
        return render(request, 'datafetch_locator/detail.html', { 'layer': getLayer } )
    except Layer.DoesNotExist:
        raise Http404("Layer does not exist")

def manage_locator(request, locator_id):
    print('id', locator_id)

    layer = get_object_or_404(Layer, pk=locator_id)
    try:
        print('choice;;', request.POST['locator_id'])
        layer.locator_set.create(locator_id=request.POST['locator_id'], locator_data=request.POST['locator_data'])
        # layer.save()

        # selected_choice = layer.locator_set.get(pk=request.POST['locator_select'])
        # print('selected choice:',selected_choice)
    except (KeyError, Layer.DoesNotExist):
        return render(request, 'datafetch_locator/detail.html', {
            'layer': layer,
            'error_message': "OPERATION FAILED",
            'choice':'blah',
        })
    else:
        return render(request, 'datafetch_locator/detail.html', {
            'layer': layer,
    })

def addLayer(request):
    """
    For adding new layer
    :param request:
    :param layerName:
    :return:
    """
    input_layer_name = request.POST['input_layer_name']
    print(input_layer_name)
    print('calling')
    layer = Layer(layer_name=input_layer_name, pub_date=timezone.now())
    layer.save()

    return render(request, 'datafetch_locator/index.html', {
            'layer': layer,
    })