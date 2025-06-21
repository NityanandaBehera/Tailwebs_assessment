from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from .forms import StudentForm, RegisterForm
from django.contrib import messages
from django.core.paginator import Paginator


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    query = request.GET.get('search')
    student_list = Student.objects.filter(teacher=request.user)
    if query:
        student_list = student_list.filter(name__icontains=query)
    paginator = Paginator(student_list, 10)  
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'home.html', {'students': students})

@login_required
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            marks = form.cleaned_data['marks']
            student, created = Student.objects.get_or_create(
                name=name, subject=subject, teacher=request.user,
                defaults={'marks': marks}
            )
            if not created:
                student.marks += marks
                student.save()
            return redirect('home')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, teacher=request.user)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id, teacher=request.user)
    student.delete()
    return redirect('home')