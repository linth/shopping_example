"""shoppingbag_origin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
# from django.urls import path

from buying import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^search/', views.search, name='search'),
    url(r'^order_form/', views.order_form, name='order_form'),
    url(r'^order_check/', views.order_check, name='order_check'),
    url(r'^order_second_check/', views.order_second_check, name='order_second_check'),

    url(r'^usa/', views.usa, name='usa'),
    # url(r'^(?P<id>\d+)/update/$', views.order_status_update_view, name='update'),
    # url(r'^productInventory/', include('productInventory.urls')),
    # url(r'^all/', views.all, name='all'),
    # url(r'^firstpay/', views.firstpay, name='firstpay'),
    # url(r'^all_goods/', views.all_goods, name='all_goods'),
    # url(r'^add/', views.add_goods, name='addgoods'),。
]
