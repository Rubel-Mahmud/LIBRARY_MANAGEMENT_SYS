from django.urls import path
from .views import create_issue, complete_issue, document_issue

urlpatterns = [
    path('<int:student_id>/create/', create_issue, name='create_issue'),
    path('<int:issue_id>/update/', complete_issue, name='complete_issue'),
    path('<int:issue_id>/document/', document_issue, name='document_issue')
]
