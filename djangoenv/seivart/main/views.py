from django.http import *
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Main site page")


def categories(request, info_id):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1>Category info</h1><p>{info_id}</p>")


def archive(request, year):
    if int(year) > 2023:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Archive by year</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>This site don't have this page, sorry(((</h1>")