from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mysite import settings
from . import views

urlpatterns = [
    url(
        r'^$', views.index,
        name='index'
    ),
    url(
        r'^accounts/login/',
        auth_views.login,
        name='login',
        kwargs={
            'template_name': './cctv/login.html'
        }
    ),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name='logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),

]