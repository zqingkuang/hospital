from django.urls import path,include
from . import views


urlpatterns = [
    path('verify_code/', views.verify_code),
    path('',views.Login.as_view(),name='login'),
]
