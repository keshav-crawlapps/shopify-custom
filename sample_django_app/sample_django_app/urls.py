"""sample_django_app URL Configuration

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
from django.urls import include, path

from shopify_app.views import callback, LoginView, uninstall
from home.views import index
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='root_path'),
    path('api/', include('api.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('auth/shopify/callback', callback, name='callback'),
    path('uninstall', uninstall, name='uninstall'),
    path('test/', include('home.urls')),
    path('webhook/product_delete', product_delete),  # WEBHOOK
    path('webhook/order_fulfilled', order_fulfilled),  # WEBHOOK
]
