from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import Student_form
from django.contrib import messages

# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def create(request):
    if request.method == 'POST':
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('index')
    else:
        form = Student_form()
    return render(request, 'form.html', {'form': form})

def update(request, pk):
    book = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = Student_form(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.info(request, 'Student updated successfully!')
            return redirect('index')
    else:
        form = Student_form(instance=book)
    return render(request, 'form.html', {'form': form})

def delete(request, pk):
    book = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.error(request, 'Student deleted successfully!')
        return redirect('index')
    return render(request, 'delete.html', {'book': book})