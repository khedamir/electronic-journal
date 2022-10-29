from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login_success, name='login_success')
]
