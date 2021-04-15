"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from service import views as service_views
import service
from django.contrib.auth import views as auth_views

service.title = 'SuperTravels';

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', service_views .home, name='home'),
    path('signup/', service_views.signup, name='signup'),
    path('login/', service_views.login, name='login'),
    path('logout/', service_views.logout, name='logout'),
]