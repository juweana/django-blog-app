from django.shortcuts import render
from .forms import ContactForm
from .models import Course, Teacher
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render



# Create your views here.
def home(request):
    return render(request, 'academy/home.html')

def courses(request):
    search = request.GET.get('search', '')
    course_list = Course.objects.filter(is_active=True).order_by('title')
    if search:
        course_list = course_list.filter(Q(title__icontains=search))
    page_obj = Paginator(course_list, 3).get_page(request.GET.get('page'))
    return render(request, 'academy/courses.html', {'page_obj': page_obj, 'search': search})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    return render(request, 'academy/course_detail.html', {'course': course})

def teachers(request):
    return render(request, 'academy/teachers.html', {'teachers': Teacher.objects.all()})

def contact (request):
    form = ContactForm(request.POST or None)
    done = request.method == 'POST' and form.is_valid()
    return render(request, 'academy/contact.html', {'form': form, 'done': done}) 