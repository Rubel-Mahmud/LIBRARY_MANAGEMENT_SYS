from django.shortcuts import render, redirect
from librarians.models import Librarian
from students.models import Student
from .models import BookIssue
from books.models import Book

def create_issue(request, student_id):
    librarian = Librarian.objects.get(pk=1)
    student = Student.objects.get(pk=student_id)
    issue = BookIssue.objects.create(student=student, librarian=librarian)
    return redirect('complete_issue', issue.pk)


# def complete_issue(request, issue_id):
#     queryset = {}
#     issue = BookIssue.objects.get(pk=issue_id)
#     books = Book.objects.filter(department=issue.student.department).filter(semister=issue.student.semister)
#     queryset['books'] = books
#     queryset['issue'] = issue
#     if request.method == "POST":
#         key_data = request.POST.keys()
#         list_data = list(key_data)
#         for i in range(1,len(list_data)):
#             book = Book.objects.get(pk=list_data[i])
#             print('book : ', book.name)
#             print('book id : ', list_data[i])
#             issue.books.add(book)
#             book.amount -= 1
#             book.save()
#             print('issue books : ', issue.books.all())
#         return redirect('document_issue', issue_id)
#     return render(request, 'book_issues/complete_issue.html', queryset)


def complete_issue(request, issue_id):
    queryset = {}
    issue = BookIssue.objects.get(pk=issue_id)
    books = Book.objects.filter(department=issue.student.department).filter(semister=issue.student.semister)
    queryset['books'] = books
    queryset['issue'] = issue
    queryset['issued_books'] = issue.books.all()
    if request.method == "POST":
        book_id = request.POST.get('book')
        book = Book.objects.get(pk=book_id)
        print('issue.books before add book : ', issue.books.all())
        if book.amount != 0:
            if book not in issue.books.all():
                issue.books.add(book)
                book.amount -= 1
                book.save()
        print('issue.books after add book : ', issue.books.all())
        # return redirect('document_issue', issue_id)
    return render(request, 'book_issues/complete_issue.html', queryset)


def document_issue(request, issue_id):
    issue = BookIssue.objects.get(pk=issue_id)
    context = {}
    context['issue'] = issue
    return render(request, 'book_issues/document_issue.html', context)

def remove_issued_book(request, issue_id, book_id):
    issue = BookIssue.objects.get(pk=issue_id)
    book = Book.objects.get(pk=book_id)
    issue.books.remove(book)
    book.amount += 1
    book.save()
    return redirect('complete_issue', issue_id)

def book_issues(request):
    context = {}
    issues = BookIssue.objects.all().order_by('-issue_date')
    context['issues'] = issues
    return render(request, 'book_issues/issues.html', context)
