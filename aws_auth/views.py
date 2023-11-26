from rest_framework.response import Response
from rest_framework.decorators import api_view
from aws_auth.serializers import BookSerializer, UserFileSerializer
from aws_auth.models import Book, UserFile
import boto3
from botocore.client import Config
from django.conf import settings


def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


def get_book(request, id):
    book = Book.objects.get(id=id)
    serializer = BookSerializer(book)
    return Response(serializer.data)


def post_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


def delete_all_books(request):
    Book.objects.all().delete()
    return Response({'success': 'All books deleted'})


@api_view(['GET'])
def insert_books(request):
    book1 = Book(title='The Hobbit', author='J.R.R. Tolkien')
    book1.save()

    book2 = Book(title='The Lord of the Rings', author='J.R.R. Tolkien')
    book2.save()

    book3 = Book(title='The Silmarillion', author='J.R.R. Tolkien')
    book3.save()

    return Response({'success': 'Books inserted'})


@api_view(['GET', 'POST', 'DELETE'])
def handle(request, id=None):
    if request.method == 'GET':
        if id:
            return get_book(request, id)
        else:
            return get_books(request)
    elif request.method == 'POST':
        return post_book(request)
    elif request.method == 'DELETE':
        return delete_all_books(request)
    else:
        return Response({'error': 'Invalid request method'})


def post_file(request):
    data = request.data

    if 'file' not in data:
        return Response({'error': 'No file found'})
    
    file = data['file']
    file_name = file.name

    user_file = UserFile(file_name=file_name, file=file)
    user_file.save()

    return Response({'success': 'File uploaded'}, status=200)


def get_files(request):
    materials = UserFile.objects.all()
    serializer = UserFileSerializer(materials, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_file(request, id):
    s3 = boto3.client(
        service_name='s3',
        region_name=settings.AWS_REGION_NAME,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        
        config=Config(signature_version='s3v4')
    )

    bucket_name = settings.AWS_S3_BUCKET_NAME
    key = UserFile.objects.get(id=id).file.name

    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        ExpiresIn=10,
        Params={
            'Bucket': bucket_name,
            'Key': key
        }
    )

    return Response({'url': url}, status=200)


@api_view(['GET', 'POST'])
def handle_files(request):
    if request.method == 'GET':
        return get_files(request)
    elif request.method == 'POST':
        return post_file(request)
    else:
        return Response({'error': 'Invalid request method'})