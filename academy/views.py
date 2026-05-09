from django.shortcuts import render
from .forms import ContactForm
from .models import Course, Teacher


# Create your views here.
def home(request):
    return render(request, 'academy/home.html')

def courses(request):
    return render(request, 'academy/courses.html' ,{ 'courses': Course.objects.all()})

def teachers(request):
    return render(request, 'academy/teachers.html', {'teachers': Teacher.objects.all()})

def contact (request):
    form = ContactForm(request.POST or None)
    done = request.method == 'POST' and form.is_valid()
    return render(request, 'academy/contact.html', {'form': form, 'done': done}) 