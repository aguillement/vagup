from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, render_to_response


def index(request):
    return render_to_response('index.html')

def generator(request):
    return render(request, 'generator/generate.html')