from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Document
from .forms import DocumentForm


from .models import Manager

# Create your views here.
@login_required
def index(request):
    context = {

    }
    #if request.user.username == "admin":
    #    return HttpResponse(request.user.username)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

    return render(request, 'cctv/index.html', context)

def login(request):

    return render(request, 'cctv/login.html')

def logout(request):

    return render(request, 'cctv/logout.html')