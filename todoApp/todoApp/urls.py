from django.contrib import admin
from django.urls import path
from tarefas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar'),
    path('editar/<int:id>/', views.editar, name='editar'),
    path('atualizar/<int:id>/', views.atualizar, name='atualizar'),
    path('deletar/<int:id>/', views.deletar, name='deletar'),
    path('concluir/<int:id>/', views.concluir, name='concluir'),
    path('desconcluir/<int:id>/', views.desconcluir, name='desconcluir'),

]