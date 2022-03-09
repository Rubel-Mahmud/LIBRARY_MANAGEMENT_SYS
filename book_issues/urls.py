from django.urls import path
from .views import (create_issue, complete_issue, document_issue,
                    remove_issued_book, book_issues, close_issue)

urlpatterns = [
    path('list/', book_issues, name='issue_list'),
    path('<int:student_id>/create/', create_issue, name='create_issue'),
    path('<int:issue_id>/update/', complete_issue, name='complete_issue'),
    path('<int:issue_id>/document/', document_issue, name='document_issue'),
    path('<int:issue_id>/close/', close_issue, name='close_issue'),
    path('<int:issue_id>/remove/<int:book_id>/', remove_issued_book, name='remove_issued_book')
]
