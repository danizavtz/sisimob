#coding: utf-8
from django.conf.urls import include, url
from . import views
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^cadastro$', views.cadastro, name='cadastro'),
	url(r'^login$', views.login_view, name='login_view'),
	url(r'^logout$', views.logout_view, name='logout_view'),
	url(r'^listview$', views.imoveis_view, name='imoveis_view'),
	url(r'^cadastro/(?P<pk>\d+)$',views.detail,name='detail'),
]