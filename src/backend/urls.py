"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path

from api.views import HomeView, HelloAPIView, AboutView, DateAPIView

djangourlpatterns = [
    path("api/admin/", admin.site.urls),
    re_path(r"^api/hello/", HelloAPIView.as_view(), name="hello"),
    re_path(r"^api/date/", DateAPIView.as_view(), name="date"),
    re_path(r"^api/about/$", AboutView.as_view(), name="about"),
]


reacturlpatterns = [
    re_path(r"^$", HomeView.as_view(), name="home"),
    re_path(r"^about/$", HomeView.as_view(), name="about"),
]

urlpatterns = djangourlpatterns + reacturlpatterns
