from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from core.forms import StudentCreationForm
from .models import Student, Department

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


def create_student(request):
    context = {}
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentCreationForm()
        context['form'] = form
    return render(request, 'students/create_student.html', context)


def students(request):
    context = {}
    students = Student.objects.all()
    context['semisters'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
    context['departments'] = Department.objects.all()

    studentId = request.GET.get('studentId')
    studentName = request.GET.get('studentName')
    department = request.GET.get('department')
    semister = request.GET.get('semister')
    mobile = request.GET.get('mobile')

    if studentId:
        students = Student.objects.filter(stdId__contains=studentId)
    if studentName:
        students = Student.objects.filter(name__icontains=studentName)
    if department and department != 'Dep':
        students = Student.objects.filter(department=department)
    if semister and semister != 'Sem':
        students = Student.objects.filter(semister=semister)
    if mobile:
        students = Student.objects.filter(mobile__contains=mobile)

    paginator = Paginator(students, 10) # Show 10 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context['page_obj'] = page_obj
    return render(request, 'students/students.html', context)

def departments(request):
    context = {}
    departments = Department.objects.all()
    context['departments'] = departments
    return render(request, 'students/departments.html', context)
