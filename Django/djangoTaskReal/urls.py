from django.contrib import admin
from django.urls import path, include
from adminpanel import views
urlpatterns = [
    path('home/', include('userpanel.urls')),  # User panel URLs will be prefixed with /home/
    path('admin/', include('adminpanel.urls')),  # Custom admin panel URLs will be prefixed with /admin/

]
