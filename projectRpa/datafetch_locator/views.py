from django.shortcuts import get_object_or_404, render
from django.http import Http404

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
        return render(request, 'datafetch_locator/details.html', { 'layer': getLayer } )
    except Layer.DoesNotExist:
        raise Http404("Layer does not exist")
