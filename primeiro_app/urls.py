# minha_app/urls.py
from django.urls import path
from . import views # <-- Importa as views do arquivo views.py desta aplicação

urlpatterns = [
    path('login/', views.login,name='login'),
    path('', views.home_view, name='home'), # Mapeia a URL raiz desta aplicação ('' ) para a função home_view
]