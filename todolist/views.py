from django.shortcuts import render, redirect, get_object_or_404
from .models import Todolist
from .forms import TodolistForm
# Create your views here.

def index(request):
    todos = Todolist.objects.all()
    form = TodolistForm
    if request.method == 'POST':
        form = TodolistForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'todos':todos, 'form':form}
    return render(request, 'index.htm', context)

def delete(request, id):
    try:
        todo = get_object_or_404(Todolist, pk=id)
    except Todolist.DoesNotExist():
        raise Http404('Task does not exist')
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    context = {'todo':todo}
    return render(request,'delete.htm', context)

def update(request, id):
    try:
        todo = get_object_or_404(Todolist, pk=id)
    except Todolist.DoesNotExist():
        raise Http404('Task does not exist')
    if request.method == 'POST':
        # pass the instance of the object (todo) to avoid creation of a new form
        form = TodolistForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/')
    form = TodolistForm(instance=todo)
    context = {'form':form}
    return render(request, 'update.htm', context)
