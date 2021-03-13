from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class Allcourses(models.Model):
    # course name
    coursename = models.CharField(max_length=200)
    # instructor name
    insname = models.CharField(max_length=100)
    startedfrom = models.DateTimeField('Started from')

    # When defining a function inside a class,
    # we need to use the (self) parameter:
    # The below function will return the coursename instead of the object id
    def __str__(self):
        return self.coursename

    # datetime from django libary
    # timezone from django.utils
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.startedfrom <= now


class details(models.Model):
    # Each class that has been created here is a sub-class of the django.db.models.Model
    # ForeignKey connects this subclass to main class. ForeignKey defines a relationship.
    # Inherits Allcourse method
    # on_delete: in case we delete any course present in 'Allcourses',
    #           we want to delete the details of that function as well
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    # ct = course type
    ct = models.CharField(max_length=500)
    # your_choice specifies option selected by user
    your_choice = models.BooleanField(default=False)
    # sp = self-paced course: used to specify the topics present in the course
    # sp = models.CharField(max_length=500)
    # il = instructor-led courses
    # il = models.CharField(max_length=500)

    # When defining a function inside a class,
    # we need to use the (self) parameter:
    def __str__(self):
        # Return the primary key of course
        return str(self.ct)
