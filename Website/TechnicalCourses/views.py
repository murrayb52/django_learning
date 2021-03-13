from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
    # This fetches the Allcourses object corresponding to course_id passed into detail()
    course = get_object_or_404(Allcourses, pk=course_id)
    # This returns the html page using the detail.html template with course (variable set above)
    # set passed as the 'course' parameter in the html file
    return render(request, 'TechnicalCourses/detail.html', {
            # 'parameter':variable
            'course':course,
    })
    '''
    #return HttpResponse('<h2>These are the course details</h2>')
    try:
        course = Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course Not Available")
    return render(request, 'TechnicalCourses/detail.html',{'course':course})
    '''


def yourchoice(request, course_id):
    # get_object_or_404 is a method
    course=get_object_or_404(Allcourses, pk=course_id)
    # use try except in case a course type DNE
    try:
        selected_ct=course.details_set.get(pk=request.POST['choice'])
    except (KeyError, Allcourses.DoesNotExist):
        return render(request, 'TechnicalCourses/detail.html',{
            'course':course,
            'error_message':"Select a valid option, dumbass",
        })
    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request, 'TechnicalCourses/detail.html', {
            'course':course
        })
