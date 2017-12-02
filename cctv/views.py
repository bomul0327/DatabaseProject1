from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import Manager

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'cctv/index.html', context)

def login(request):

    return render(request, 'cctv/login.html')

def logout(request):

    return render(request, 'cctv/logout.html')