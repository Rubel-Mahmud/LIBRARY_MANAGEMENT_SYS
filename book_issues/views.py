from django.shortcuts import render, redirect
from librarians.models import Librarian
from students.models import Student
from .models import BookIssue
from books.models import Book

def book_issue(request, student_id):
    librarian = Librarian.objects.get(pk=1)
    student = Student.objects.get(pk=student_id)
    issue = BookIssue.objects.create(student=student, librarian=librarian)
    return redirect('book_issue_complete', issue.pk)


def book_issue_complete(request, book_issue_id):
    queryset = {}
    issue = BookIssue.objects.get(pk=book_issue_id)
    books = Book.objects.filter(department=issue.student.department).filter(semister=issue.student.semister)
    queryset['books'] = books
    queryset['issue'] = issue
    if request.method == "POST":
        key_data = request.POST.keys()
        list_data = list(key_data)
        for i in range(1,len(list_data)):
            book = Book.objects.get(pk=list_data[i])
            print('book : ', book.name)
            print('book id : ', list_data[i])
            issue.books.add(book)
            book.amount -= 1
            book.save()
            print('issue books : ', issue.books.all())
        return redirect('book_issue_document', book_issue_id)
    return render(request, 'book_issues/book_issue.html', queryset)


def book_issue_document(request, book_issue_id):
    issue = BookIssue.objects.get(pk=book_issue_id)
    context = {}
    context['issue'] = issue
    return render(request, 'book_issues/book_issue_document.html', context)
