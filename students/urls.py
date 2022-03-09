from django.urls import path
from .views import students, departments

urlpatterns = [
    path('list/', students, name='student_list'),
    path('departments/list/', departments, name='department_list')
]
