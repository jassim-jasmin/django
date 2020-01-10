from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Layer, Locator
from django.template import loader

def index(request):
    layerArray = Layer.objects.order_by('-pub_date')[:5]
    print(layerArray)

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': layerArray,
    }
    return HttpResponse(template.render(context, request))

def getLocatorId(request, locator_id):
    return HttpResponse("Locator id: %s" % locator_id)

def layerData(request, layer_id):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    layerObject = Layer.objects.order_by('-pub_date')#[:5]
    # layerDataObject = Layer.objects.get(layer_name=layer_id)
    # locatorDataArray = layerDataObject.locator_set.all()

    # output = ', '.join(t.locator_id+'::'+t.locator_data for t in locatorDataArray)
    layerArray = Layer.objects.order_by('-pub_date')  # [:5]
    return HttpResponse(layerArray)
