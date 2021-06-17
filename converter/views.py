from django.http.response import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.

key1 = "636d309899e0cc52dfc97276b08774cfa68e9e2d"
url1 = "https://api.getgeoapi.com/v2/currency/list"
key2 = "226f17e7fe20f207c512"
url2 = "https://free.currconv.com/api/v7/convert"

def index(request):
    return render(request, "index.html")

def graph(request):
    parameters = {"q": "USD_INR", "compact": "ultra", "date": "2021-01-01", "endDate": "2021-01-08", "apiKey": key2}
    response = requests.get(url2, parameters)
    context = {"data": response.json()}
    return render(request, "graph.html", context)


