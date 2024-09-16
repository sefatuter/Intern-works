from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin_view, name='signin'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # Logout URL
    path('todo/', todo_view, name='todo'),
    path('todo/add/', add_todo, name='add_todo'),
    path('todo/edit/<int:id>/', edit_todo, name='edit_todo'),
    path('todo/delete/<int:id>/', delete_todo, name='delete_todo'),
    path('todo/toggle_complete/<int:id>/', toggle_complete, name='toggle_complete'),
]