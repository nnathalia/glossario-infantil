from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('corpo_humano', views.corpo_humano, name='corpo_humano'),
  path('apresentacao', views.apresentacao, name='apresentacao'),
  path('como_usar', views.como_usar, name='como_usar'),
  path('palavra/<int:id>/', views.palavra, name='palavra'),
  path('autores', views.autores, name='autores'),
  path('ficha_tecnica', views.ficha_tecnica, name='ficha_tecnica')
]