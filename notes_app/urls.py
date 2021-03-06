"""notes_app URL Configuration


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
from django.contrib import admin
from django.urls import path, include
from django.urls import include, path

from  api import views

urlpatterns = [
    path('',  include('api.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    path('faq/', include('api.urls')), 
    path('polls/', include('polls.urls')),
    path('home/',  include('yellowpage.urls')),
   
    
    
     # add this line
]