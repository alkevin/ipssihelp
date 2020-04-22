from django.urls import re_path, path
from . import views

app_name = 'worker'

urlpatterns = [
    path('', views.home, name='home'),
    path('user', views.users, name='users'),
    path('ad', views.ad_list, name='ad_list'),
    path('ad/supply', views.ad_supply, name='ad_supply'),
    path('ad/demand', views.ad_demand, name='ad_demand'),
    re_path(r'ad/([0-9]+)/', views.ad_details, name='ad_details'),
]