from django.conf.urls import url
from . import views


#cctv/views.py에서 정의된 def 함수명(request)에서 함수명을 아래에 url(regular expresstion, views.함수명, name='함수명'),으로 추가하기
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^shoot_space_manage$', views.shoot_space_manage, name='shoot_space_manage'),
    url(r'^file_manage$', views.file_manage, name='file_manage'),
    url(r'^log_read$', views.log_read, name='log_read'),
    url(r'^my_page$', views.my_page, name='my_page'),
    url(r'^manager_manage$', views.manager_manage, name='manager_manage'),
    url(r'^cctv_manage$', views.cctv_manage, name='cctv_manage'),
    url(r'^space_manage$', views.space_manage, name='space_manage'),
    #url(r'^post/new/$', views.post_new, name='post_new') # forms.py 을 위하여 추가한 것
]
