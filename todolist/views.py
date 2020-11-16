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

def detail(request, id):
    try:
        todo = get_object_or_404(Todolist, pk=id)
    except Todolist.DoesNotExist():
        raise Http404('Task does not exist')
    context = {'todo':todo}
    return render(request,'detail.htm', context)