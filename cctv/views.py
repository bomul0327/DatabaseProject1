from django.shortcuts import render

#여기에 def로 정의한 함수 cctv/urls.py에도 추가하기
def list(request):
    return render(request, 'cctv/shoot_space_manage.html', {})

# Create your views here.
