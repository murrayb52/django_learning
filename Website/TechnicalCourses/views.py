from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader

# Create your views here.
def Courses(request):
    # ac = all course
    ac = Allcourses.objects.all()
    template = loader.get_template('TechnicalCourses/Courses.html')
    # context is a dictionary-mapping template variable name to python objects
    context = {
        # store all the elements (e.g. courses) that are present
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request,course_id):
    #return HttpResponse('<h2>These are the course details</h2>')
    try:
        course = Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course Not Available")
    return render(request, 'TechnicalCourses/detail.html',{'course':course})