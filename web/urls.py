from django.conf.urls import url
from web import views

urlpatterns = [
  url(r'^listado/', views.listado, name='listado'),
  url(r'^herbario/', views.HerbarioPDF.as_view(), name='herbario'),
  url(r'^points.data/', views.plantas_json, name='points'),
  url(r'^$', views.MainPageView, name='mapa'), 
]
