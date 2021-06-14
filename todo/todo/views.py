from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Todo
from .forms import TodoForm

# index
def index(request):
  todo_list = Todo.objects.order_by('id')
  form = TodoForm()
  context = {'todo_list': todo_list, 'form': form}
  return render(request, 'todo/index.html', context)

# add
@require_POST
def addTodo(request):
  form = TodoForm(request.POST)
  if form.is_valid():
    new_todo = Todo(text=request.POST['text'])
    new_todo.save()
  return redirect('index')

# complete
def completeTodo(request, todo_id):
  todo = Todo.objects.get(pk=todo_id)
  # todo.complete = True
  todo.complete = not(todo.complete)
  todo.save()
  return redirect('index')

#del completed
def deleteCompleted(request):
  Todo.objects.filter(complete__exact=True).delete()
  return redirect('index')

# del all
def deleteAll(request):
  Todo.objects.all().delete()
  return redirect('index')

# add Pokus
def addPokus(request):
  new_todo = Todo(text='Pokus')
  new_todo.save()
  return redirect('index')

# Invert
def Invert(request):
  for todo in Todo.objects.all():
    todo.complete = not(todo.complete)
    todo.save()

  # TOTO Nefunguje protoze se updatuje querySet prubezne
  # Django: change the value of a field for all objects in a queryset - https://is.gd/eKqaT6
  # Python/Django how to avoid to update a queryset object in memory while update the database - https://is.gd/mxSMt1
  # qsT = Todo.objects.all().filter(complete=True)
  # qsF = Todo.objects.all().filter(complete=False)
  # qsT.update(complete=False)
  # qsF.update(complete=True)
  return redirect('index')
