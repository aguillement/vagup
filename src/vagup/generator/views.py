import os
import csv

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from datetime import datetime


def index(request):
    return render_to_response('index.html')


def generator(request):
    return render(request, 'generator/generate.html')


def generated(request):
    u"""User clicked on generate, get form and generate Vagrantfile."""

    response = HttpResponse(content_type='text')
    response['Content-Disposition'] = 'attachment; filename="Vagrantfile"'

    response.write("First row" + "\n")
    response.write("Second row")

    return response
