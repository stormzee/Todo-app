from django.shortcuts import render
from .models import Todolist
# Create your views here.

def index(request):
    todos = Todolist.objects.all()
    context = {'todos':todos}
    return render(request, 'index.html', context)

def delete_todo(request, id):
    return render('/')