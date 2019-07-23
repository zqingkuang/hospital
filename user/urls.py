from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('verify_code/', views.verify_code),
    path('', views.Login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('quit/', views.quit, name='quit'),
    path('role_index/', views.role_index, name='role_index'),
    path('role_jurisdiction/<int:sid>/', views.role_jurisdiction, name='role_jurisdiction'),
    path('user_index/', views.user_index, name='user_index')

]
