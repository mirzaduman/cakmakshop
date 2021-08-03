from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('marka/', views.marka, name='marka'),
    path('arama/', views.arama, name='arama'),
    path('<int:no>', views.cakmak, name='cakmak'),
    path('plastik/', views.plastik, name='plastik'),
    path('metal/', views.metal, name='metal'),
    path('tasli/', views.tasli, name='tasli'),
    path('manyetolu/', views.manyetolu, name='manyetolu'),
    path('rezistansli/', views.rezistansli, name='rezistansli'),
    path('iletisim/', views.iletisim, name='iletisim')
]
