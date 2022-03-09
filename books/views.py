from django.core.paginator import Paginator
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
    paginator = Paginator(books, 5) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    return render(request, 'books/book_list.html', context)
