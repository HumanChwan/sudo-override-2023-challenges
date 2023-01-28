from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('create_blog', create_blog, name='create_blog'),
    path('view_blog', view_blog, name='view_blog'),
    path('blog/<int:id>', handle_single_view, name='handle_single_view'),
]