from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from userpanel.models import Todo


def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:  # Only allow admin/staff users to login
            login(request, user)
            return redirect('admin_dashboard')  # Redirect to the admin dashboard
        else:
            messages.error(request, 'Invalid credentials or unauthorized access')
    return render(request, 'admin_login.html')


@login_required
def admin_dashboard(request):
    users = User.objects.all()  # Fetch all users
    print(users)
    return render(request, 'admin_dashboard.html', {'users': users})  # Use render instead of redirect


@login_required
def admin_add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            user.is_staff = True  # Make sure to mark them as staff/admin if necessary
            user.save()
            messages.success(request, 'User created successfully')
            return redirect('admin_dashboard')
        else:
            messages.error(request, 'Username already exists')
    return render(request, 'admin_add_user.html')


@login_required
def admin_edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        messages.success(request, 'User updated successfully')
        return redirect('admin_dashboard')
    return render(request, 'admin_edit_user.html', {'user': user})


@login_required
def admin_delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully')
        return redirect('admin_dashboard')
    return render(request, 'admin_delete_user.html', {'user': user})


@login_required
def user_todos(request, user_id):
    user = get_object_or_404(User, id=user_id)
    todos = Todo.objects.filter(user=user)  # Assuming you have a user field in your Todo model
    return render(request, 'user_todos.html', {'user': user, 'todos': todos})