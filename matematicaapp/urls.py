from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('estudante/<int:pk>/', views.estudante_detail, name='estudante_detail'),
    path('estudante/novo/', views.estudante_novo, name='estudante_novo'),
    path('estudante/<int:pk>/edit/', views.estudante_edit, name='estudante_edit'),
    path('atividadesgratis', views.atividadesgratis, name='atividadesgratis'),
    path('atividades5ano/<int:pk>/<int:id_resposta>/', views.atividades5ano, name='atividades5ano'),
]