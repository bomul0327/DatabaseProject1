from django.conf.urls import url
from django.contrib.auth import views as auth_views

from mysite import settings
from . import views

urlpatterns = [
    url(
        r'^$', views.index,
        name='index'
    ),

]