from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

urlpatterns += [
    url(r'^mycartidges/$', views.ClientCartridgeRepairs.as_view(), name='cartridges'),
]