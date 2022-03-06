from django.shortcuts import render
from books.models import Book

# def book_totall(request):
#     totall = 0
#     context = {}
#     books = Book.objects.all()
#     for book in books:
#         totall += book.amount
#     context['totall'] = totall
#     return render(request, 'base.html', context)

def book_list(request):
    context = {}
    books = Book.objects.all()
    context['books'] = books
    return render(request, 'books/book_list.html', context)
