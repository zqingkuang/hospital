"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from registration import views

urlpatterns = [

    path('index/',views.index,name='r_index'),
    path('add/',views.add,name='add'),
    path('look/<int:sid>',views.look,name='look'),
    path('edit/<int:sid>',views.edit,name='edit'),
    path('delete/<int:sid>',views.delete,name='delete'),
    path('registrations/<int:page_no>',views.registrations,name='page_no'),
    path('hospital/',views.h_index,name='h_index'),
    path('adds',views.adds,name='adds'),


]
