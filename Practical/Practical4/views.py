# Practical4/views.py
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def student_form(request):
    if request.method == 'POST':
        if 'submit' in request.POST:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('Practical4:student_form')
        elif 'show_database' in request.POST:
            return redirect('Practical4:view_database')
    else:
        form = StudentForm()
    return render(request, 'Practical4/student_form.html', {'form': form})

def view_database(request):
    students = Student.objects.all()
    return render(request, 'Practical4/view_database.html', {'students': students})
