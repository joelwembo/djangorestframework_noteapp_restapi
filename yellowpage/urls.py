from django.urls import path
from . import views

# direct to view home conents
urlpatterns = [
    path('', views.home, name='yellowpage-home'),
  
]
