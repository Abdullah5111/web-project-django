from django.shortcuts import render
from .forms import StudentForm

def signup_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()

    return render(request, 'signup_student.html', {'form': form})
