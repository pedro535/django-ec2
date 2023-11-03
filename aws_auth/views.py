from rest_framework.response import Response
from rest_framework.decorators import api_view
from aws_auth.serializers import BookSerializer
from aws_auth.models import Book


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


