from django.urls import path
from django.conf.urls import url

from django.views.generic import TemplateView
from . import views

# direct to view home conents
urlpatterns = [
    path('', views.home, name='yellowpage-home'),
    path('connection/', views.login, name='yellowpage-login'),

  
]
