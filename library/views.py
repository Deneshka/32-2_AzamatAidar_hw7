from django.shortcuts import render
from . import models

def Books_Library_View(request):
    book = models.Books_Library.objects.all()
    return render(request, 'books.html', {'book_key': book})

