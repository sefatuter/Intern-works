from django.urls import path
from .views import (
    admin_login, admin_dashboard, admin_add_user,
    admin_edit_user, admin_delete_user, user_todos
)


urlpatterns = [
    path('', admin_login),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('add-user/', admin_add_user, name='admin_add_user'),
    path('edit-user/<int:user_id>/', admin_edit_user, name='admin_edit_user'),
    path('delete-user/<int:user_id>/', admin_delete_user, name='admin_delete_user'),
    path('user-todos/<int:user_id>/', user_todos, name='user_todos'),
]





