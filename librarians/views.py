from django.shortcuts import render
from students.models import Student

def home(request):
    context = {}
    students = Student.objects.all()
    context['students'] = students
    return render(request, 'librarians/home.html', context)
