from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
# Create your views here.


def index(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'index.html', {'tarefas': tarefas})

def adicionar(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        nova_tarefa = Tarefa.objects.create(titulo=titulo)
        return redirect('editar', id=nova_tarefa.id)

def editar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    return render(request, 'editar.html', {'tarefa': tarefa})

def atualizar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    if request.method == 'POST':
        tarefa.titulo = request.POST['titulo']
        tarefa.descricao = request.POST.get('descricao', '')
        tarefa.prioridade = request.POST.get('prioridade', 'medio')
        tarefa.save()
        return redirect('index')

def deletar(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.delete()
    return redirect('index')

def concluir(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.feita = True
    tarefa.save()
    return redirect('index')

def desconcluir(request, id):
    tarefa = get_object_or_404(Tarefa, id=id)
    tarefa.feita = False
    tarefa.save()
    return redirect('index')