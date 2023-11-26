from django.contrib import admin
from django.urls import path
from aws_auth.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', handle, name='handle'),
    path('api/v1/books/<int:id>/', handle, name='handle'),
    path('api/v1/insert/', insert_books, name='insert_books'),
    path('api/v1/files/', handle_files, name='files'),
    path('api/v1/files/<int:id>/', get_file, name='get_file'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
