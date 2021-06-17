from django.http.response import HttpResponse
from django.shortcuts import render
import json
import requests

# Create your views here.

key1 = "636d309899e0cc52dfc97276b08774cfa68e9e2d"
url1 = "https://api.getgeoapi.com/v2/currency/list"
key2 = "226f17e7fe20f207c512"
url2 = "https://free.currconv.com/api/v7/convert"

def index(request):
    return render(request, "index.html")

def graph(request):
    from_to = "EUR_INR"
    params = {"apiKey": key2, "compact": "ultra", "q": from_to, "date": "2021-01-01", "endDate": "2021-01-08"}
    response = requests.get(url2, params)
    response_data = response.json()
    labels = list(response_data[from_to].keys())
    data = list(response_data[from_to].values())
    context = {"labels": labels, "data": data}
    return render(request, "graph.html", context)


