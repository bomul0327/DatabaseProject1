from django.shortcuts import render
from .models import Manager, Shoot_space, CCTV, Shoot, Files, Neighborhood, Sequence, Statistics, Record #DB Table과 HTML을 연결해주는 역할
#테이블 이름은 cctv_'객체명' , eg: cctv_manager, cctv_shoot_space ...

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def login(request):
    return render(request, 'cctv/login.html', {})

def shoot_space_manage(request):
    return render(request, 'cctv/shoot_space_manage.html', {})

def file_manage(request):
    return render(request, 'cctv/file_manage.html', {})

def log_read(request):
    return render(request, 'cctv/log_read.html', {})

def my_page(request):
    return render(request, 'cctv/my_page.html', {})

def manager_manage(request):
    manager_list = Manager.objects.raw('select id, pos, phonenum from cctv_manager')
    return render(request, 'cctv/user_manage.html', {'manager_list' : manager_list})

def cctv_manage(request):
    return render(request, 'cctv/cctv_manage.html', {})

def space_manage(request):
    return render(request, 'cctv/space_manage.html', {})

# Create your views here.
