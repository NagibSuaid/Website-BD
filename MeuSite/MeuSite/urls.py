"""MeuSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import include
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contatos/', include('contatos.urls')),
    path('accounts/', views.homeSec, name="sec-home"),
    path('accounts/registro/', views.registro, name= 'sec-register'),
    path('accounts/login/', LoginView.as_view(template_name='registro/login.html'), name='sec-login'),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy("sec-home")), name='sec-logout'),
    path('accounts/profile/', views.paginaPerfil, name='sec-profile'),
]
