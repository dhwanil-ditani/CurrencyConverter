from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

key = "636d309899e0cc52dfc97276b08774cfa68e9e2d"

def index(request):
    parameters = {"api_key": key, "format": "json"}
    url = "https://api.getgeoapi.com/v2/currency/list"
    response = requests.get(url, parameters)
    return HttpResponse(response)


