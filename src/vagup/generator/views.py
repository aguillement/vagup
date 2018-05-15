import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from datetime import datetime


def index(request):
    return render_to_response('index.html')


def generator(request):
    return render(request, 'generator/generate.html')


def generated(request):
    filename = "./views.py"
    with open(filename, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/text')
        response['Content-Disposition'] = 'attachment; filename=' + filename
        response['Content-Type'] = 'application/text; charset=utf-8'
        return response
