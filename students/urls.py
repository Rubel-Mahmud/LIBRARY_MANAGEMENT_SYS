from django.urls import path
from .views import students

urlpatterns = [
    path('list/', students, name='student_list'),
]
