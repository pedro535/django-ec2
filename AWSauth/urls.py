from django.contrib import admin
from django.urls import path
from aws_auth.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', handle, name='handle'),
    path('books/<int:id>/', handle, name='handle'),
    path('insert/', insert_books, name='insert_books'),
    path('files/', handle_files, name='files'),
    path('files/<int:id>/', get_file, name='get_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
