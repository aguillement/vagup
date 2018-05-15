
from django.http import HttpResponse
from django.shortcuts import render, render_to_response

from .forms import VagrantForm


def index(request):
    return render_to_response('index.html')


def generator(request):
    u"""Generate vagrantfile."""

    if request.method == 'POST':
        form = VagrantForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            response = HttpResponse(content_type='text')
            response['Content-Disposition'] = 'attachment; filename="Vagrantfile"'

            response.write("First row" + "\n")
            response.write("Second row")

            return response
    else:
        form = VagrantForm()

    return render(request, 'generator/generate.html', {'form': form})
