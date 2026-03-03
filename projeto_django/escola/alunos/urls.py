from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_alunos),
    path('detalhe/', views.detalhe_aluno),
    path('novo/', views.cadastrar_aluno),
]