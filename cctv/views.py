from django.shortcuts import render

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def shoot_space_manage(request):
    return render(request, 'cctv/shoot_space_manage.html', {})

def file_manage(request):
    return render(request, 'cctv/file_manage.html', {})

def log_read(request):
    return render(request, 'cctv/log_read.html', {})

def my_page(request):
    return render(request, 'cctv/my_page.html', {})

def user_manage(request):
    return render(request, 'cctv/user_manage.html', {})

def cctv_manage(request):
    return render(request, 'cctv/cctv_manage.html', {})

def space_manage(request):
    return render(request, 'cctv/space_manage.html', {})

# Create your views here.
