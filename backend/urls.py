"""backend URL Configuration

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
from django.conf import settings

from landing.views import HomeView
from django.views.generic import TemplateView

urlpatterns = [
    path(str(settings.ADMIN_URL), admin.site.urls),
    path('', HomeView.as_view()),
    path('404', TemplateView.as_view(template_name='404.html')),
    path('*', TemplateView.as_view(template_name='404.html')),
]

handler404 = 'landing.views.custom_404'
handler500 = 'landing.views.custom_500'