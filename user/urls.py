from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('verify_code/', views.verify_code),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
    path('quit/', views.quit, name='quit'),
    path('role_index/', views.role_index, name='role_index'),
    path('role_jurisdiction/<int:sid>/', views.role_jurisdiction, name='role_jurisdiction'),
    path('user_index/', views.user_index, name='user_index'),
    path('user_deletes/',views.user_deletes, name='user_deletes'),
    path('user_delete/<int:sid>/', views.user_delete, name='user_delete'),
    path('user_editUser/<int:sid>/', views.user_editUser, name='user_editUser'),
    path('password/<int:sid>',views.password,name='password'),
    url('', views.Login, name='login')

]
