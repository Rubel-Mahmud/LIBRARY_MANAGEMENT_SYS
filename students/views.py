from django.shortcuts import render
from .models import Student

# def home2(request):
#     queryset = {}
#     if request.method == 'POST':
#         student_id = request.POST.get('student_id')
#         try:
#             student = Student.objects.get(stdId=student_id)
#             queryset['student'] = student
#         except Student.DoesNotExist:
#             message = 'No student found'
#             queryset['message'] = message
#         print('student_id : ', student_id)
#     else:
#         students = Student.objects.all()
#         queryset['students'] = students
#     return render(request, 'students/home.html', queryset)


def students(request):
    context = {}
    students = Student.objects.all()
    context['students'] = students
    return render(request, 'students/students.html', context)
