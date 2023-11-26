from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)

class UserFile(models.Model):
    id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
