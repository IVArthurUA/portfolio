from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Main site page")


def categories(request, info_id):
    return HttpResponse(f"<h1>Category info</h1><p>{info_id}</p>")