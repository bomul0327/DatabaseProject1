from django.shortcuts import render

def list(request):
    return render(request, 'cctv/html/shoot_space_manage.html', {})

# Create your views here.
