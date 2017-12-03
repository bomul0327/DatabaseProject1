from django.conf.urls import url
from . import views


#cctv/views.py에서 정의된 def 함수명(request)에서 함수명을 아래에 url(regular expresstion, views.함수명, name='함수명'),으로 추가하기
urlpatterns = [
    url(r'^$', views.list, name='list'),
]
