from django.contrib import admin
from django.urls import path
from . import views

# URLs for the Technical Courses app
app_name = 'TechnicalCourses'
urlpatterns = [
    # path('', [name-of-function], name='[name-of-page])
    path('<int:course_id>/',views.detail, name='detail'),
    path('', views.Courses, name='home-page'),
    path('<int:course_id>/yourchoice/', views.yourchoice, name='yourchoice'),
]