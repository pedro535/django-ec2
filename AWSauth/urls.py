from django.contrib import admin
from django.urls import path
from aws_auth.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', handle, name='handle'),
    path('api/v1/books/<int:id>/', handle, name='handle'),
    path('api/v1/insert/', insert_books, name='insert_books'),
    
]
