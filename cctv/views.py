from django.shortcuts import render

def post_list(request):
    return render(request, 'cctv/html/shoot_space_manage.html', {})

# Create your views here.
