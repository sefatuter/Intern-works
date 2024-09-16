# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *
from django.shortcuts import get_object_or_404, redirect
from .models import Todo


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def signin_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})


@login_required  # Restrict access to authenticated users
def todo_view(request):
    return render(request, 'todo.html')


def home(request):
    return render(request, 'home.html')


@login_required
def todo_view(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo.html', {'todos': todos})



@login_required
def add_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo')
    else:
        form = TodoForm()
    return render(request, 'add_todo.html', {'form': form})


@login_required
def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'edit_todo.html', {'form': form})

@login_required
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo')
    return render(request, 'confirm_delete.html', {'todo': todo})



def toggle_complete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo')
