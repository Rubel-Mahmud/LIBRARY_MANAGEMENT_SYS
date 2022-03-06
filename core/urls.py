from django.contrib import admin
from django.urls import path, include
from book_issues.views import book_issue_complete, book_issue, book_issue_document
from books.views import book_list
from librarians.views import home

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home view
    path('', home, name='home'),

    path('students/', include('students.urls')),

    # Book Issue
    path('book_issues/<int:student_id>/', book_issue, name='book_issue'),

    # Complete Book issue
    path('book_issues/<int:book_issue_id>/update/', book_issue_complete, name='book_issue_complete'),
    path('book_issues/<int:book_issue_id>/document/', book_issue_document, name='book_issue_document'),

    # path('', totall_book, name='totall_book'),

    path('books/list/', book_list, name='book_list'),
]
