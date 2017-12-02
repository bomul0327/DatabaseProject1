from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Manager

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'cctv/index.html', context)