from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Sub_Counties, Incidences
# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

def sub_county_dataset(request):
    sub_counties = serialize('geojson', Sub_Counties.objects.all())
    return HttpResponse(sub_counties, content_type='json')

def incidences_dataset(request):
    incidence = serialize('geojson', Incidences.objects.all())
    return HttpResponse(incidence, content_type='json')