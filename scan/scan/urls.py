"""
URL configuration for scan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import scan_page,start_page,info_users,info_users_id,info_users_viewset
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register (r"api_vs",info_users_viewset)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("scan_page",scan_page,name="home_page"),
    path("",start_page,name="start_page"),
    path("api/",info_users.as_view()),
    path("api/<pk>/",info_users_id.as_view()),
] + router.urls
