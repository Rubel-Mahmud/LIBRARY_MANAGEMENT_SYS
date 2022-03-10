from django.urls import path
from .views import create_student, students, departments

urlpatterns = [
    path('create/', create_student, name='create_student'),
    path('list/', students, name='student_list'),
    path('departments/list/', departments, name='department_list')
]
