"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as auth_views
from rest_framework.documentation import include_docs_urls

from user import views as user_views

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Acompanha legis docs', public=False)),
    path('auth/', auth_views.obtain_auth_token),
    path('register/', user_views.RegisterView.as_view()),
    path('profile/', user_views.ProfileView.as_view()),
    path('reset_password/', user_views.ResetPasswordView.as_view()),
    path('', include(router.urls)),
]
