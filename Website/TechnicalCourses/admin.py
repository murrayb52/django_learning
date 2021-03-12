from django.contrib import admin

# Register your models here.
from .models import Allcourses, details

# These are the classes that will be made available to the admin page
admin.site.register(Allcourses)
admin.site.register(details)