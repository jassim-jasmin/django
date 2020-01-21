from django.shortcuts import get_object_or_404, render
from django.http import Http404

from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from .models import Layer, Layer_Connect, Layer_Validation
from django.template import loader

def layerMain(request):
    layerName = Layer.objects.order_by('layer_name')
    layerJson = { 'layer_name' : layerName}

    return render(request, 'datafetch_locator/layer_main.html', layerJson)

def locatorMain(request, layer):
    layer = Layer.objects.get(pk=request.POST['layer'])
    # locator = layer.objects.locator_set.filter(layer_name=layer)
    print(layer)

    return HttpResponse('call success')

def index(request):
    return HttpResponse('hello')
#     """
#     todo Need to perform other operation for index page
#     :param request:
#     :return:
#     """
#     layerArray = MainClass.objects.order_by('-pub_date')[:5]
#     context = {
#         'layer_list': layerArray,
#     }
#     return render(request, 'datafetch_locator/index.html', context)
#
# def getAllLayer(request):
#     """
#     Returns all layers available
#     todo Change to profile wise layer
#     :param request:
#     :return: layer list in index.html
#     """
#     layerArray = MainClass.objects.order_by('-pub_date')[:5]
#     context = {
#         'layer_list': layerArray,
#     }
#     return render(request, 'datafetch_locator/index.html', context)
#
# def getLocatorId(request, locator_id):
#     return HttpResponse("Locator id: %s" % locator_id)
#
# def layerData(request, layer_id):
#     """
#     Purpose of this function is, based on layer_name corresponding locators need to return
#     :param request:
#     :param layer_id: layer name
#     :return: locator coresponding layer
#     """
#     try:
#         getLayer = get_object_or_404(MainClass, layer_name=layer_id)
#         return render(request, 'datafetch_locator/detail.html', { 'layer_list': getLayer } )
#     except MainClass.DoesNotExist:
#         raise Http404("Layer does not exist")
#
# def manage_locator(request, locator_id):
#     print('id', locator_id)
#
#     layer = get_object_or_404(MainClass, pk=locator_id)
#     try:
#         print('choice;;', request.POST['locator_id'])
#         layer.locator_set.create(locator_id=request.POST['locator_id'], locator_data=request.POST['locator_data'])
#         # layer.save()
#
#         # selected_choice = layer.locator_set.get(pk=request.POST['locator_select'])
#         # print('selected choice:',selected_choice)
#     except (KeyError, MainClass.DoesNotExist):
#         return render(request, 'datafetch_locator/detail.html', {
#             'layer_list': layer,
#             'error_message': "OPERATION FAILED",
#             'choice':'blah',
#         })
#     else:
#         return render(request, 'datafetch_locator/detail.html', {
#             'layer_list': layer,
#     })
#
# def addLayer(request, layer_list):
#     """
#     For adding new layer
#     :param request:
#     :param layerName:
#     :return:
#     """
#     input_layer_name = request.POST['input_layer_name']
#     print('adding layer', input_layer_name)
#     print('calling')
#     layer = MainClass(layer_name=input_layer_name, pub_date=timezone.now())
#     layer.save()
#     layer_list = MainClass.objects.order_by
#
#     return render(request, 'datafetch_locator/index.html', {
#             'layer_list': layer_list,
#     })
#
# def deleteLayer(reques, layer_list):
#     print('delete layer')
#     return HttpResponse('success')