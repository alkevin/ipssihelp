from django.urls import re_path
from . import views

app_name = 'worker'

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^user$', views.users, name='user'),
    re_path(r'^ad$', views.ads, name='ad'),
    re_path(r'^ad/supply$', views.ads_supply, name='supply'),
    re_path(r'^ad/demand$', views.ads_demand, name='demand'),
    re_path(r'^ad/([0-9]+)/$', views.ad_details, name='detail'),
]