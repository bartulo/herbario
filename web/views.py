from django.http import HttpResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import TemplateView
from web.models import *

def listado(request):
  plantas = Planta.objects.order_by('familia__nombre')
  return render(request, 'listado.html', {'plantas': plantas})

def plantas_json(request):
  points_as_geojson = serialize('geojson', Planta.objects.all())
  return HttpResponse(points_as_geojson, content_type='json')

def MainPageView(request):
  plantas = Planta.objects.all()
  return render(request, 'index.html', {'plantas': plantas})
